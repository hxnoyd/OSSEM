# {{entry['title']}}
{{entry['description']}}

## Data Fields
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
{%- for row in entry['data fields'] %}
|{{row['standard name']}}|{{row['field name']}}|{{row['type']}}|{{row['description']}}|{{row['sample value']}}|
{%- endfor %}

{%- if entry['resources'] %}

## Resources
{%- for resource in entry['resources'] %}
[{{resource['text']}}]({{resource['link']}})
{%- endfor %}
{% endif %}
{%- if entry['tags'] %}
## Tags
{%- for tag in entry['resources'] %}
* {{tag}}
{%- endfor %}
{%- endif %}