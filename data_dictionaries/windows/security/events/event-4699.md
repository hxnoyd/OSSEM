# Event ID 4699: A scheduled task was deleted

## Description
This event generates every time a scheduled task was deleted.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|user_sid|SubjectUserSid|string|SID of account that requested the "delete scheduled task" operation. |ORG\UserA|
|user_name|SubjectUserName|string|the name of the account that requested the "delete scheduled task" operation.|UserA|
|user_domain|SubjectDomainName|string|subject's domain or computer name.|ORG|
|user_logon_id|SubjectLogonId|integer|hexadecimal value that can help you correlate this event with recent events that might|contain|
||TaskContent|string|the XML of the deleted task.|<?xml version="1.0" encoding="UTF-16"?>   2015-08-25T13:56:10.5315552 CONTOSO\\dadmin     LeastPrivilege CONTOSO\\dadmin Password    IgnoreNew false true false false false  true false  true true false false false PT0S 7    C:\\Windows\\notepad.exe   </Data>|
||TaskName|string|deleted scheduled task name.|\task_path\task_name|

## Resources
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4699.md)
* [MS Security Auditing Category - Object Access](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#object-access)
* [MS Security Auditing Sub-category - Audit Other Object Access Events](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-other-object-access-events.md)

## Tags
* Object Access
* Audit Other Object Access Events