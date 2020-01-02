# Event ID 17: PipeEvent (Pipe Created)

## Description
This event generates when a named pipe is created. Malware often uses named pipes for interprocess communication.<a href="https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon#event-id-17-pipeevent-pipe-created">https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon#event-id-17-pipeevent-pipe-created</a>

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|tag|RuleName|string|custom tag mapped to event. i.e ATT&CK technique ID|T1114|
|event_date_creation|UtcTime|date|Time in UTC when event was created|4/11/18 6:21|
|process_guid|ProcessGuid|string|Process Guid of the process that created the pipe|{A98268C1-A968-5ACD-0000-0010BD4EC200}|
|process_id|ProcessId|integer|Process ID used by the os to identify the process that created the pipe|1224|
|pipe_name|PipeName|string|Name of the pipe created|Anonymous Pipe|
|process_name|Image|string|File name of the process that created the pipe|cmd.exe|
|process_path|Image|string|File path of the process that created the pipe|C:\WINDOWS\system32\cmd.exe|

## Resources
* [Sysmon Source](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon#event-id-17-pipeevent-pipe-created)
