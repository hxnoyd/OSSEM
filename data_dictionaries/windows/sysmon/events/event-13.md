# Event ID 13: RegistryEvent (Value Set)

## Description
This Registry event type identifies Registry value modifications. The event records the value written for Registry values of type DWORD and QWORD.<a href="https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon#event-id-13-registryevent-value-set">https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon#event-id-13-registryevent-value-set</a>

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|tag|RuleName|string|custom tag mapped to event. i.e ATT&CK technique ID|T1114|
|event_type|EventType|string|registry event. Registry values modifications|SetValue|
|event_date_creation|UtcTime|date|Time in UTC when event was created|4/11/18 6:04|
|process_guid|ProcessGuid|string|Process Guid of the process that modified a registry value|{A98268C1-95F9-5ACD-0000-001025861000}|
|process_id|ProcessId|integer|Process ID used by the os to identify the process that that modified a registry value|4624|
|process_name|Image|string|File name of the process that that modified a registry value|Explorer.EXE|
|process_path|Image|string|File path of the process that that modified a registry value|C:\WINDOWS\Explorer.EXE|
|registry_key_path|TargetObject|string|complete path of the registry key|HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Notifications\Data\418A073AA3BC3475|
|registry_key_details|Details|string|Details added to the registry key|Binary Data|

## Resources
* [Sysmon Source](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon#event-id-13-registryevent-value-set)
