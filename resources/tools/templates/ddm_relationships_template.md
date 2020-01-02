# {{entry['title']}}
{{entry['description']}}

## Data Fields
{% if entry['title'] == 'Data Object Relationships' %}
|Sub Data Sources|Data Objects (Origin)|Relationship|Data Objects (Destination)|
|---|---|---|---|
{%- for row in entry['data fields'] %}
|{{row['sub data sources']}}|{{row['data objects (origin)']}}|{{row['relationship']}}|{{row['data objects (destination)']}}|
{%- endfor %}
{% else %}
|ATT&CK Data Source|Sub Data Source|Source Data Object|Relationship|Destination Data Object|EventID|
|---|---|---|---|---|---|
{%- for row in entry['data fields'] %}
|{{row['att&ck data source']}}|{{row['sub data source']}}|{{row['source data object']}}|{{row['relationship']}}|{{row['destination data object']}}|{{row['eventid']}}|
{%- endfor %}
{% endif %}

{% if entry['resources'] %}
## Resources
{%- for resource in entry['resources'] %}
[{{resource['text']}}]({{resource['link']}})
{%- endfor %}
{% endif %}
{% if entry['tags'] %}
## Tags
{%- for tag in entry['resources'] %}
* {{tag}}
{%- endfor %}
{% endif %}