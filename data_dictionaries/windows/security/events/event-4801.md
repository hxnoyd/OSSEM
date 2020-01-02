# Event ID 4801: The workstation was unlocked

## Description
This event is generated when workstation was unlocked.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|user_sid|TargetUserSid|string|SID of account that requested the "unlock workstation" operation|S-1-5-21-3457937927-2839227994-823803824-1104|
|user_name|TargetUserName|string|the name of the account that requested the "unlock workstation" operation.|dadmin|
|user_domain|TargetDomainName|string|subject's domain or computer name.|CONTOSO|
|user_logon_id|TargetLogonId|integer|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID,|0x759a9|
|session_id|SessionId|integer|unique ID of unlocked session.|3|

## Resources
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4801.md)
* [MS Security Auditing Category - Account Logon](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#account-logon)
* [MS Security Auditing Category - Logon/Logoff](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#logonlogoff)
* [MS Security Auditing Sub-category - Audit Other Logon/Logoff Events](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-other-logon/logoff-events.md)

## Tags
* Account Logon
* Logon/Logoff
* Audit Other Logon/Logoff Events