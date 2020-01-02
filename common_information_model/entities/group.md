# Group Schema
Event fields used to define metadata about a security group, or distribution group that is created changed or deleted.

## Data Fields
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|group_name||string|the name of a security group, or a distribution group that is created, changed, or deleted|AccountOperators|
|group_domain||string|domain or computer name of the group|CONTOSO|
|group_sid||string|SID of a group|S-1-5-21-3457937927-2839227994-823803824-6605|
|group_sam_name||string|this is a name of the group used to support clients and servers from previous versions of Windows (pre-Windows 2000 logon name). The value of sAMAccountName attribute of new group object. For example: ServiceDesk. For local groups it is simply a name of new group|AccountOperators|
|group_sid_history||string|contains previous SIDs used for the object if the object was moved from another domain. Whenever an object is moved from one domain to another, a new SID is created and becomes the objectSID. The previous SID is added to the sIDHistory property. This parameter contains the value of sIDHistory attribute of a group object. This parameter might not be captured in the event, and in that case appears as "-". For local groups it is not applicable and always has "-" value.|-|