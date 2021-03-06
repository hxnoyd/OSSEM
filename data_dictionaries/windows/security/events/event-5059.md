# Event ID 5059: Key migration operation.

## Description

This event generates when a cryptographic key is exported or imported using a Key Storage Provider.

## Data Dictionary

|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|user_sid|SubjectUserSid|string|SID of account that requested key migration operation.|S-1-5-21-3457937927-2839227994-823803824-1104|
|user_name|SubjectUserName|string|the name of the account that requested key migration operation.|dadmin|
|user_domain|SubjectDomainName|string|subject's domain or computer name.|CONTOSO|
|user_logon_id|SubjectLogonId|string|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID, for example, "4624: An account was successfully logged on."|0x38e2d|
|key_provider_name|ProviderName|string|the name of KSP through which the operation was performed.|Microsoft Software Key Storage Provider|
|key_algorithm_name|AlgorithmName|string|the name of cryptographic algorithm through which the key was used or accessed.|ECDH\_P521|
|key_name|KeyName|string|the name of the key (key container) with which operation was performed.|le-SuperAdmin-795fd6c1-2fae-4bef-a6bc-4f4d464bc083|
|key_type|KeyType|string|can have one of the following values: "User key." – user's cryptographic key. "Machine key." – machine's cryptographic key.|%%2500|
|key_operation|Operation|string|performed operation.|%%2464|
|key_return_code|ReturnCode|integer|has "0x0" value for Success events.|0x0|

## Reference

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/public/windows/security/threat-protection/auditing/event-5059.md)