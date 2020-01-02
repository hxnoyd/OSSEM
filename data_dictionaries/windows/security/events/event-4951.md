# Event ID 4951: A rule has been ignored because its major version number was not recognized by Windows Firewall.

## Description
When you create or edit a Windows Firewall rule, the settings that you can include depend upon the version of Windows you use when creating the rule.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|profile|Profile|string|the name of the profile of the ignored rule.|All|
|rule_id|RuleId|string|the unique identifier for ignored firewall rule.|{08CBB349-D158-46BE-81E1-2ABC59BDD523}|
|rule_name|RuleName|string|the unique identifier for ignored firewall rule.|-|

## Resources
[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/public/windows/security/threat-protection/auditing/event-4951.md)
[MS Security Auditing Category - Policy Change](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#policy-change)
[MS Security Auditing Sub-category - Audit MPSSVC Rule-Level Policy Change](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-mpssvc-rule-level-policy-change.md)

## Tags
* Policy Change
* Audit MPSSVC Rule-Level Policy Change