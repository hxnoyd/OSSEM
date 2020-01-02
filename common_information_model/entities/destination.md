# Destination Schema
Event fields used to define the destination (server) in a network connection event.

## Data Fields
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|dst_bytes||integer|network bytes sent by the dst_ip_addr|100|
|dst_host_name||string|The destination server, host, hostname, domain, or domain name. Some examples, would include the TLS server name, HTTP Host, DNS Query Name, etc. For information on how to define and use this field refer to the documentation additional-guidelines/domain_or_hostname_or_fqdn.md|www.google.com|
|dst_domain||string|If there is a clear distinction of the domain VS hostname VS FQDN this is the domain field. More often than not this should NOT be used and should be defined in the ./target.md, ./host.md, or ./user.md. However, you may follow the recommendations additional-guidelines/domain_or_hostname_or_fqdn.md if there is a clear example for this|bigwheel.corporation.local|
|dst_fqdn||string|If there is a clear distinction of the domain VS hostname VS FQDN this is the FQDN field. More often than not this should NOT be used and should be defined in the ./target.md, ./host.md, or ./user.md. However, you may follow the recommendations additional-guidelines/domain_or_hostname_or_fqdn.md if there is a clear example for this|bob-berto-pc.bigwheel.corporation.local|
|dst_ip_addr||ip|Destination IP address|8.8.8.8|
|dst_ip_bytes||integer|network IP (header) bytes sent by the dst_ip_addr|104|
|dst_mac||mac|Destination MAC address|a9:68:82:28:c4:6d|
|dst_mime_type||string|MIME type as seen in (layer 7) application layer details or as defined by a application scanner such as an anti-virus/EDR. For HTTP this is usually from the server's "Content-Type" header. For some examples of MIME types, check out: https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Complete_list_of_MIME_types|application/pdf|
|dst_packets||integer|Network packets sent by the dst_ip_addr|5|
|dst_port||integer|Destination port number|138|
|dst_port_name||string|Destination port name. This is usually determined by IANA common port assignment. Therefore, this means its a guess and NOT the actual the application used|netbios-dgm|