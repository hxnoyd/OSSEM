# Services Table

## Description
List all installed Windows services and their relevant data.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|service_name|name|TEXT|Service name||
|service_type|service_type|TEXT|Service Type: OWN_PROCESS, SHARE_PROCESS and maybe Interactive (can interact with the desktop)||
|service_display_name|display_name|TEXT|Service Display name||
|service_status|status|TEXT|Service Current status: STOPPED, START_PENDING, STOP_PENDING, RUNNING, CONTINUE_PENDING, PAUSE_PENDING, PAUSED||
|process_id|pid|INTEGER|the Process ID of the service||
|service_start_type|start_type|TEXT|Service start type: BOOT_START, SYSTEM_START, AUTO_START, DEMAND_START, DISABLED||
|service_error_code|win32_exit_code|INTEGER|The error code that the service uses to report an error that occurs when it is starting or stopping||
|service_exit_code|service_exit_code|INTEGER|The service-specific error code that the service returns when an error occurs while the service is starting or stopping||
|file_path|path|TEXT|Path to Service Executable||
|module_path|module_path|TEXT|Path to ServiceDll||
|service_description|description|TEXT|Service Description||
|user_name|user_account|TEXT|The name of the account that the service process will be logged on as when it runs. This name can be of the form Domain\UserName. If the account belongs to the built-in domain, the name can be of the form .\UserName.||

## Resources
* [osquery GitHub](https://github.com/facebook/osquery/blob/master/specs/windows/services.table)
