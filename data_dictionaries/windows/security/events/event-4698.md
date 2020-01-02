# Event ID 4698: A scheduled task was created

## Description
This event generates every time a new scheduled task is created.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|user_sid|SubjectUserSid|string|SID of account that requested the "create scheduled task" operation. |S-1-5-21-3457937927-2839227994-823803824-1104|
|user_name|SubjectUserName|string|the name of the account that requested the "create scheduled task" operation.|UserName|
|user_domain|SubjectDomainName|string|subject's domain or computer name.|DOMAIN|
|user_logon_id|SubjectLogonId|integer|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID|0x364eb|
||TaskContent|string|the XML content of the new task.|<?xml version="1.0" encoding="UTF-16"?>   2015-09-22T19:03:06.9258653 CONTOSO\\dadmin     LeastPrivilege CONTOSO\\dadmin InteractiveToken    IgnoreNew true true true false false  true false  true true false false false P3D 7    C:\\Documents\\listener.exe   </Data>|
||TaskName|string|new scheduled task name.|\Microsoft\StartListener|

## Resources
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4698.md)
* [MS Security Auditing Category - Object Access](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#object-access)
* [MS Security Auditing Sub-category - Audit Other Object Access Events](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-other-object-access-events.md)

## Tags
* Object Access
* Audit Other Object Access Events