#!/usr/bin/python
# Author: Fred Frey (@fryguy2600)
# Date: Oct 14, 2019
# Description: Scrape OSSEM Data Dictionary Markdown files and create YAML data struct files
#               for scripts to use
# Usage:
#   scrape_dictionary.py  -d ./OSSEM/data_dictionaries/
# Output:
#   event-1.md -> "Data Dictionary" -> event-1.yml

import os
import csv
import re
import sys
import yaml
from collections import defaultdict
from pathlib import Path
import argparse

# todo add asserts to make sure data dictionary is standardized/reliable

column_names = ["Product", "Standard Name", "Field Name", "Type", "Description", "Sample Value"]

def get_file_list(path):
    if os.path.isfile(path) and path.endswith('.md'):
        return([path])
    else: 
        return(list(Path(path).rglob("*.md")))

def get_data_dictionary(data):
    '''Given a path to a file, read file line by line and detect/carve out the Data Dictionary
        Return a list of lists (2D array) of Data Dictionary with line 0 being column headers and
        following lines being data elements '''

    data_dict = []
    capture = False

    # Read each line, carve out Data Dictionary after seeing Markdown header ## Data Dictionary
    #with open(file, 'r', encoding='utf-8') as data:

    for line in data: #.readlines():
        if line.startswith('## Data Dictionary'):
            capture = True
            #print('found it')
        elif not line.replace('-','').replace('|','').strip():
            # Skip blank lines and lines only containing dashes
            pass
        elif capture and not line.startswith('|'):
            capture = False
            print('ending it')
        elif capture:
            # Strip whitespace and drop first/last junk column
            junk = [x.strip()  for x in line.split('|')[1:-1]]
            data_dict.append(junk)
        else:
            pass
            
    return(data_dict)   # [['column1_header','column2_header'], ['data_row1_col1', 'data_row1_col2'], ['data_row2_col1', 'data_row2_col2'] ]

def array_to_dict(data_dict_array):
    data_dict = {}
    headers = data_dict_array[0]

    for row in data_dict_array[1:]:
        temp = dict(zip(headers, row))
        data_dict[temp.pop('Field Name')] = temp

    return(data_dict)

def get_description(data):
    desc = False
    desc_text = ''
    for line in data:

        if '## Description' in line:
            desc = True
        elif '## ' in line and desc:
            return(desc_text) # once we leave, return all description
        elif desc and len(line)>2:
            # If we are in description text block, capture lines
            desc_text += line 
        


def create_arg_parser():
    """"Creates and returns the ArgumentParser object."""

    parser = argparse.ArgumentParser(description='Description of your app.')
    parser.add_argument('-d', '--data_dict_dir', type=Path,
                    help='Path to the OSSEM Data Dictionary root')
    return parser

def extract_string(text, pattern):
    try:
        #print(text, pattern)

        m = re.search(pattern, str(text), flags=re.DOTALL)
        #print("Found: ", len(m.groups))
        found = m.group(1)
    except:
        found = ''
        print("WARN: Couldn't find ", pattern)
    
    return(found)



if __name__ == "__main__":
    data_dict = []
    master_csv = []
    mydict = lambda: defaultdict(mydict)

    arg_parser = create_arg_parser()
    parsed_args = arg_parser.parse_args(sys.argv[1:])
    
    if not (parsed_args.data_dict_dir and os.path.exists(parsed_args.data_dict_dir)):
        print("ERROR: Provide -d path_to_data_dictionary\n")
        arg_parser.print_help()
        sys.exit()

    files = get_file_list(parsed_args.data_dict_dir)

    # Scrape Markdown files. Build master dict and optionally dump individual Data Dict as CSVs 
    for filename in files:
        print(filename)
        metadata = {}
        product = 'unknown' 
        
        with open(filename, 'r', encoding='utf-8') as openfile:
            data = openfile.readlines()

            #print(data)
            # Scrape all Markdown return 2D Array of data dictionary
            data_dict = get_data_dictionary(data)

            if len(data_dict):

                # Parse actual Data Dictionaries from Array to Dict
                metadata['eventData'] = array_to_dict(data_dict)

                # Get Filename
                file_base = os.path.basename(filename).replace('.md', '')
                #print(file_base)

                # Get OS (ie: windows) and Product (ie sysmon) from Directory path
                # ie ../data_dictionaries/windows/windowsdefenderatp/AlertEvents.md
                if(not 'data_dictionaries' in str(filename)):
                    print("ERROR: -d DATA_DICT_DIR, --data_dict_dir DATA_DICT_DIR ... must include the 'data_dictionaries' dir to anchor us")
                    sys.exit(1)

                m = re.search(r'data_dictionaries[\\\\/](\S+?)[\\\\/](\S+)[\\\\/]\S+\.md', str(filename))

                if m.group(1) and m.group(2):
                    metadata['platform'] = m.group(1)
                    product = m.group(2).replace('\\', '_').replace('/', '_') # might be nested
                    
                    # Below is geared towards Sysmon and Windows events, try and find the info
                    metadata['name']            = extract_string(data, r'title: Event ID \d+ - (.*?)\\n')
                    metadata['logtype']         = extract_string(data, r'log.type: (.*?)\\n')
                    metadata['author']          = extract_string(data, r'author: (.*?)\\n')
                    metadata['date']            = extract_string(data, r'date: (.*?)\\n')
                    metadata['providerGUID']    = extract_string(data, r'Guid="{(.*?)}"')
                    metadata['description']     = extract_string(data, r'description: (.*?)\\n')
                    metadata['provider']        = extract_string(data, r'Provider Name="(.*?)"')
                    metadata['channel']         = extract_string(data, r'<Channel>(.*?)</Channel>')
                    metadata['details']         = get_description(data)


                    try:
                        metadata['eventID']         = int(extract_string(file_base, r'-(\d+)'))
                    except:
                        pass

                    if(not metadata['name']):
                        metadata['title']                  = extract_string(data, r'# (Event ID \d+)')
                        metadata['name']                   = extract_string(data, r'# (Event ID .*?)\\n')
                        metadata['description']            = extract_string(data, r'# Event ID \d+: (.*?)\\n')
                        metadata['logtype']                = product

                    if 'carbonblack' in str(filename):
                        metadata['title']            = extract_string(data, r'# (ingress.*?)\\n')
                        metadata['name']             = file_base

                        metadata['provider'] = 'carbonblack'


                else:
                    print("Error: matching os and product")
                    sys.exit(1)

                
                # Write metadata out to YAML file in same directory as Markdown
                with open(str(filename).replace('.md', '.yml'), 'w') as outfile:
                    outfile.write(yaml.dump(metadata, default_flow_style=False))
        
