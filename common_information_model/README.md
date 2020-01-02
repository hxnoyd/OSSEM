# Common Information Model

## Description
The common information model facilitates the normalization of data sets by providing a standard way to parse security event logs. It is organized by specific entities associated with event logs and defined in more details by Data Dictionaries. The definitions of each entity and its respective field names are mostly general descriptions that could help and expedite event logs parsing procedures.

## Sub Data Sets
|entities|Description|Tags|
|---|---|---|
|[Alert Schema](entities/README.md)|Alert fields that describe an indicator from a tool of a possible issue.||
|[Any Schema](entities/README.md)|Fields used to define metadata for a single field to include data from multiple fields with similar/same values/data.  This data is most commonly created from an ETL pipeline.<br> Any fields below that contain a '*' indicates those are searches and not actual fields (key/values). This is because certain values are not desirable to copy/duplicate. However, because of a common schema we can still find are values for a specific common type, without duplicating or copying everything to one field!  ||
|[Destination Schema](entities/README.md)|Event fields used to define the destination (server) in a network connection event.||
|[Destination NAT Schema](entities/README.md)|Event fields used to define the destination NAT (network address translation) in a network connection event.||
|[DNS Schema](entities/README.md)|Event fields used to define metadata in DNS events. This commonly incudes data in logs that contain DNS queries.  Including, but not limited to, Zeek dns.log, Suricata DNS, Sysmon EventID 22, Windows DNS debug/trace logs.<br> In the verbiage below, request is used to denote the client (or fowarded address if applicable) that is making the DNS request. This would commonly be the client/source that is looking up a domain.<br> The response/answer, is used to denote the server that responded with the answer or responded to the request/client.<br> It is important to remember that in DNS logs their are multiple servers that may be involved in the response. This is similar to how packets are forwarded through routers.||
|[Event Schema](entities/README.md)|Event fields used to define specific metadata of the event itself. For example, event_id or event_creation_time.||
|[File Schema](entities/README.md)|Event fields used to define metadata about files either locally or over the wire.||
|[Flow Schema](entities/README.md)|Flow fields will be ported to source.md, destination.md, and network.md for continuity. Also, the first flow spec (created by cisco) use Source/Destination terminology.||
|[Group Schema](entities/README.md)|Event fields used to define metadata about a security group, or distribution group that is created changed or deleted.||
|[Hash Schema](entities/README.md)|Event fields used to define metadata about hashes.||
|[Host Schema](entities/README.md)|Event fields used to define metadata about hosts where events are originally created.||
|[HTTP Schema](entities/README.md)|Event fields used to define metadata about HTTP information. This is based on information in the layer 7 (HTTP) application, however can also include HTTP information from an endpoint/server. IIS, Apache, NGINX, proxy logs, and other variances of logs that have HTTP information would go in here. Also, if the HTTP connection is from a decrypted/MITM HTTPS/TLS session then portions of that information, where applicable, would go in here.||
|[IP Schema](entities/README.md)|Event fields used to define metadata about IP addresses in a network. It follows the standard from the Destination and Source categories.||
|[Kerberos TGS Schema](entities/README.md)|Event fields used to define Kerberos Ticket Granting Service.||
|[Kerberos TGT Schema](entities/README.md)|Event fields used to define Kerberos Ticket Granting Tickets.||
|[Logon Schema](entities/README.md)|Event fields used to define metadata about logon events.||
|[MAC Schema](entities/README.md)|Event fields used to define metadata about MAC addresses in a network. It follows the standard from the Destination and Source categories.||
|[Meta Schema](entities/README.md)|Added fields that are derived from an event's data/fields after it is has been logged or stored and more specifically could change based on future information. In the simplest form, this would include enrichments of the data. A good example, would be the Autonomous System Number lookup of an IP address. The reason, is because an IP address on 2018-01-01 may belong to one entity and the later in the future could be acquired by a new entity and thus the data from 2018-01-01 may be different than say 2022-01-01. Actually, a great example of this example is the IP address <code>1.1.1.1</code> that for a long time belonged to APNIC, and then was acquired by Cloudflare in 2019. The Meta schema, is a way that can help aide an analyst to know the field they are looking at may be derived from a data source or calculation that could change over time.||
|[Module Schema](entities/README.md)|Event fields used to define metadata about modules in an endpoint.||
|[Network Schema](entities/README.md)|Event fields used to define metadata about network information seen in a typical OSI layer. This includes data both from an endpoint as well as a network monitoring device/application (NSM, Firewall, IPS, IDS, etc...). This differentiates from data that is specific to Source and Destination specific information such as Source or Destination bytes, packets, IP address, mac address, TCP flags.||
|[Pipe Object](entities/README.md)|Event fields used to define metadata about pipes being created or connected in an endpoint.||
|[Port Schema](entities/README.md)|Event fields used to define metadata about ports in a network connection.||
|[Process Schema](entities/README.md)|Event fields used to define metadata about processes in an system.||
|[Registry Key Schema](entities/README.md)|Event fields used to define metadata about registry entries in a system.||
|[Software Schema](entities/README.md)|None||
|[Source Schema](entities/README.md)|Event fields used to define the source (client) in a network connection event.||
|[Source NAT Schema](entities/README.md)|Event fields used to define the source NAT (network address translation) in a network connection event.||
|[Target](entities/README.md)|Event fields used to define entities being targeted by other entities locally in a system. This is different from a network connection event. It is more related to events that involve relationships defined locally by entities such as files, processes,users, etc.||
|[TLS Schema](entities/README.md)|Event fields used to define metadata about a TLS(SSL) record.<br> Work in progress...||
|[URL Schema](entities/README.md)|Event fields used to define metadata about a URL/URI. There is a lot of ambiguity from the community on the difference URL vs URI. Granted, URL would normally include the domain, port (if applicable), user, password, query, fragment, and URI. However, there are many scenarios from log sources where one could not distinguish whether it was the full URL or just the URI.<br> URL data can be seen in various log sources as defined in http.md as well as other applications such as SIP. URLs, especially in HTTP, have a best practice implementation however it is not necessary to adhere for connections/data to be established.||
|[User Shema](entities/README.md)|Event fields used to define metadata about users in an network environment.||
|[User Agent Schema](entities/README.md)|Event fields used to define metadata about the User-Agent header in an application. Most commonly this header/field is seen in HTTP log sources. However, can also be seen in SIP and SMTP. Work in progress...||
