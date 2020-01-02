# ingress.event.moduleload (Module Load)

## Description
This event contains the information for modules loaded by processes on endpoints monitored by Carbon Black.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|cb_sensor|cb_server|TEXT|Used to distinguish between multiple Cb Response servers. Set this in the "server_name" option of cb-event-forwarder.ini.|cbserver|
|host_name|computer_name|TEXT|hostname of the sensor|JASON-MAC-VM|
|event_type|event_type|TEXT|The type of event|modload|
|process_link|link_process|TEXT|Deep link to Cb Response UI for process|https://cbtests/#analyze/00000001-0000-07b4-01d1-209a100bc217/1|
|sensor_link|link_sensor|TEXT|Deep link to Cb Response UI for sensor|https://cbtests/#/host/1|
|hash|md5|TEXT|md5 of the module|3D136E8D4C0407D9C40FD8BDD649B587|
|file_path|path|TEXT|Path of the module loaded into the current process|/System/Library/Frameworks/Security.framework/Versions/A/PlugIns/csparser.bundle/Contents/MacOS/csparser|
|process_id|pid|INTEGER|Endpoint OS Process id of process|1972|
|process_guid|process_guid|TEXT|Cb Process GUID of process|00000001-0000-07b4-01d1-209a100bc217|
|sensor_id|sensor_id|INTEGER|sensor ID of associated sensor|1|
|event_date_creation|timestamp|INTEGER|Endpoint timestamp of this event since epoch|1447697423|
|event_type_detailed|type|TEXT|The full type of event|ingress.event.moduleload|

## Resources
* [Carbon Black Developer Docs](https://developer.carbonblack.com/reference/enterprise-response/event-forwarder/event-schema/#ingress-event-moduleload-module-load)
