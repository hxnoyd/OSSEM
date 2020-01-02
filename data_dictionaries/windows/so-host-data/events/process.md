# SO Host Data - Process Table

## Description
Get-SOHostData enumerates active processes on the scanned system. To do this it combines the output of PowerShell's Get-Process cmdlet and the Win32_Process WMI class.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|source_type|SourceType|TEXT|Type of data represented|WinEvent-Process|
|id|Id|TEXT|SO Host Data's unique identifier of this instance|BBB8A0D8A8A3EF0148FE5E4DF188E7FC39741EE4554152B9E6513FE95F4E377B|
|parent_process_key|ParentProcessKey|TEXT|SO Host Data's unique identifier of parent process|B8148C17D1C227B6D50E54CB6EF93738852340CF4682E63292F1197330BBE579|
|token_key|TokenKey|TEXT|SO Host Data's unique identifier of associated access token|8C3C0F18E053F361BF80D7BD126F67A5B7BE8241388802ABA430D751F60CD7D3|
|sha256_hash|SHA256Hash|TEXT|SHA256Hash of the process's main module on disk|CCC8538DD62F20999717E2BBAB58A18973B938968D699154DF9233698A899EFA|
|process_name|ProcessName|TEXT|Name of the process|powershell|
|process_id|ProcessId|INTEGER|Process's unique identifier|8540|
|start_time|StartTime|DATE|The time the process was started|2/20/2018 11:00:09 PM|
|path|Path|TEXT|The location of the process binary on disk|C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe|
|command_line|CommandLine|TEXT|The command string used to launch the process|"C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe"|
