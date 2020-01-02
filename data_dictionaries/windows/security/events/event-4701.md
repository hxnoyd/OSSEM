# Event ID 4701: A scheduled task was disabled

## Description
This event generates every time a scheduled task is disabled.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|user_sid|SubjectUserSid|string|SID of account that requested the "disable scheduled task" operation. |THEDOMAIN\TheUser|
|user_name|SubjectUserName|string|the name of the account that requested the "disable scheduled task" operation.|TheUser|
|user_domain|SubjectDomainName|string|subject's domain or computer name.|THEDOMAIN|
|user_logon_id|SubjectLogonId|integer|hexadecimal value that can help you correlate this event with recent events that might||
||TaskContent|string|the XML of the disabled task.|<?xml version="1.0" encoding="UTF-16"?>   2015-09-22T19:03:06.9258653 CONTOSO\\dadmin     LeastPrivilege CONTOSO\\dadmin InteractiveToken    IgnoreNew true true true false false  true false  true false false false false P3D 7    C:\\Documents\\listener.exe   </Data>|
||TaskName|string|disabled scheduled task name.|\ImportantTask|

## Resources
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4701.md)
* [MS Security Auditing Category - Object Access](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#object-access)
* [MS Security Auditing Sub-category - Audit Other Object Access Events](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-other-object-access-events.md)

## Tags
* Object Access
* Audit Other Object Access Events