# Event ID 4722: A user account was enabled

## Description
This event generates every time user or computer object is enabled.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|target_user_name|TargetUserName|string|the name of the account that was enabled.|Auditor|
|target_user_domain|TargetDomainName|string|target account's domain or computer name.|CONTOSO|
|target_user_sid|TargetSid|string|SID of account that was enabled. Event Viewer automatically tries to resolve SIDs and show the account name. If the SID cannot be resolved, you will see the source data in the event.|S-1-5-21-3457937927-2839227994-823803824-2104|
|user_sid|SubjectUserSid|string|SID of account that requested the "enable account" operation. Event Viewer automatically tries to resolve SIDs and show the account name. If the SID cannot be resolved, you will see the source data in the event.|S-1-5-21-3457937927-2839227994-823803824-1104|
|user_name|SubjectUserName|string|the name of the account that requested the "enable account" operation.|dadmin|
|user_domain|SubjectDomainName|string|subject's domain or computer name.|CONTOSO|
|user_logon_id|SubjectLogonId|integer|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID, for example, "4624: An account was successfully logged on."|0x30d5f|

## Resources
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4722.md)
* [MS Security Auditing Category - Account Management](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#account-management)
* [MS Security Auditing Sub-category - Audit User Account Management](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-user-account-management.md)

## Tags
* Account Management
* Audit User Account Management