# Event ID 4702: A scheduled task was updated

## Description
This event generates every time scheduled task was updated/changed.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|user_sid|SubjectUserSid|string|SID of account that requested the "change/update scheduled task" operation.|THEDOMAIN\UserB|
|user_name|SubjectUserName|string|the name of the account that requested the "change/update scheduled task" operation.|UserB|
|user_domain|SubjectDomainName|string|subject's domain or computer name.|THEDOMAIN|
|user_logon_id|SubjectLogonId|integer|hexadecimal value that can help you correlate this event with recent events that might|contain|
||TaskContentNew|string|the new XML for the updated task.|<?xml version="1.0" encoding="UTF-16"?>   2015-09-22T19:03:06.9258653 CONTOSO\\dadmin     HighestAvailable CONTOSO\\dadmin InteractiveToken    IgnoreNew true true true false false  true false  true true false false false P3D 7    C:\\Documents\\listener.exe   </Data>|
||TaskName|string|updated/changed scheduled task name.|\VeryImportantTask|

## Resources
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4702.md)
* [MS Security Auditing Category - Object Access](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#object-access)
* [MS Security Auditing Sub-category - Audit Other Object Access Events](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-other-object-access-events.md)

## Tags
* Object Access
* Audit Other Object Access Events