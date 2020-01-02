# macOS Carbon Black Event Logs

## Description
Carbon Black data schema as defined by the Carbon Black Developer Resources.


## Data model
![Data model](/resources/images/CarbonBlackDataModel.png)

## Sub Data Sets
|events|Description|Tags|
|---|---|---|
|[ingress.event.childproc (Child Process)](events/childproc.md)|A process has spawned another process on an endpoint monitored by Carbon Black.||
|[ingress.event.filemod (File Modification)](events/filemod.md)|A file on the filesystem has been created, deleted, or modified on an endpoint monitored by Carbon Black.||
|[ingress.event.moduleload (Module Load)](events/modload.md)|This event contains the information for modules loaded by processes on endpoints monitored by Carbon Black.||
|[ingress.event.netconn (Network Connection)](events/netconn.md)|A network connection has been received or initiated by an endpoint monitored by Carbon Black.||
|[ingress.event.procstart (Process Start)](events/proc.md)|A new process has started (or exited) on an endpoint monitored by Carbon Black.||

## Resources
* [Carboon Black Event Schema](https://developer.carbonblack.com/reference/enterprise-response/event-forwarder/event-schema/)