# Event ID 4610: An authentication package has been loaded by the Local Security Authority.

## Description
This event generates every time Authentication Package.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|logon_authentication_package_name|AuthenticationPackageName|string|the name of loaded Authentication Package. The format is: DLL_PATH_AND_NAME: AUTHENTICATION_PACKAGE_NAME.|C:\Windows\system32\msv1_0.DLL : MICROSOFT_AUTHENTICATION_PACKAGE_V1_0|

## Resources
[MS SOURCE](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/public/windows/security/threat-protection/auditing/event-4610.md)
[MS Security Auditing Category - System](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#system)
[MS Security Auditing Sub-category - Audit Security System Extension](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-security-system-extension.md)

## Tags
* System
* Audit Security System Extension