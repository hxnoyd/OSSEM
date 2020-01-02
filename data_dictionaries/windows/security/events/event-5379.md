# Event ID 5379: Credential Manager credentials were read

## Description
This event occurs when a user performs a read operation on stored credentials in Credential Manager.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|user_sid|SubjectUserSid|string|SID of account that performed a read operation on stored credentials in CM|S-1-5-18|
|user_name|SubjectUserName|string|the name of the account that performed a read operation on stored credentials in CM|ACCT001$|
|user_domain|SubjectDomainName|string|subject's domain or computer name|SHIRE|
|user_logon_id|SubjectLogonId|integer|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID|0x3e7|
|credentials_read|TargetName|string|stored credentials that were read|WindowsLive:(token):name=xxxxxasas;serviceuri=*|
|credentials_read_type|Type|integer||0|
|credential_read_returned_count|CountOfCredentialsReturned|integer||0|
|object_operation_type|ReadOperation|string||%%8100|
|credentials_read_returned_code|ReturnCode|string||0|
|process_creation_time|ProcessCreationTime|date||2019-02-25T22:33:21.621488200Z|
|process_id|ClienProcessId|integer||4432|
