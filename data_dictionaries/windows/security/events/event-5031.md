# Event ID 5031: The Windows Firewall Service blocked an application from accepting incoming connections on the network

## Description
This event generates when an application was blocked from accepting incoming connections on the network by Windows Filtering Platform. If you don't have any firewall rules (Allow or Deny) in Windows Firewall for specific applications, you will get this event from Windows Filtering Platform layer, because by default this layer is denying any incoming connections.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
||Profiles|string|Network profile using which application was blocked.|Domain|
|process_path|Application|string|Full path and file name of executable file for blocked application.|C:\documents\listener.exe|

## Resources
[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-5031.md)
[MS Security Auditing Category - Object Access](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#object-access)
[MS Security Auditing Sub-category - Audit Filtering Platform Connection](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-filtering-platform-connection.md)

## Tags
* Object Access
* Audit Filtering Platform Connection