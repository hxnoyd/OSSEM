# Windows Carbon Black Event Logs

## Description
Carbon Black data schema as defined by the Carbon Black Developer Resources.

## Data model
![Data model](/resources/images/CarbonBlackDataModel.png|width=900))

## Sub Data Sets
|events|Description|Tags|
|---|---|---|
|[ingress.event.childproc (Child Process)](events/README.md)|A process has spawned another process on an endpoint monitored by Carbon Black.||
|[ingress.event.crossprocopen (Cross Process Open)](events/README.md)|A process has attempted to open a handle into another process OR if a remote thread was created.||
|[ingress.event.emetmitigation (EMET Mitigation)](events/README.md)|Microsoft EMET has killed a process on an endpoint monitored by Carbon Black.||
|[ingress.event.filemod (File Modification)](events/README.md)|A file on the filesystem has been created, deleted, or modified on an endpoint monitored by Carbon Black.||
|[ingress.event.moduleload (Module Load)](events/README.md)|This event contains the information for modules loaded by processes on endpoints monitored by Carbon Black.||
|[ingress.event.netconn (Network Connection)](events/README.md)|A network connection has been received or initiated by an endpoint monitored by Carbon Black.||
|[ingress.event.procstart (Process Start)](events/README.md)|A new process has started (or exited) on an endpoint monitored by Carbon Black.||
|[ingress.event.processblock (Process Block)](events/README.md)|A process was blocked from executing on an endpoint monitored by Carbon Black because the process MD5 has been blacklisted.||
|[ingress.event.regmod (Registry Modification)](events/README.md)|A registry key has been created, deleted, or modified on an endpoint monitored by Carbon Black.||
|[ingress.event.tamper (Cb Response Tamper)](events/README.md)|A process tampered with a critical Carbon Black userspace process or kernel driver.||

## Resources
[Carboon Black Event Schema](https://developer.carbonblack.com/reference/enterprise-response/event-forwarder/event-schema/)