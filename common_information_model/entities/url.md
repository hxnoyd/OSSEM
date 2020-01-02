# URL Schema
Event fields used to define metadata about a URL/URI. There is a lot of ambiguity from the community on the difference URL vs URI. Granted, URL would normally include the domain, port (if applicable), user, password, query, fragment, and URI.
However, there are many scenarios from log sources where one could not distinguish whether it was the full URL or just the URI.<br>
URL data can be seen in various log sources as defined in http.md as well as other applications such as SIP. URLs, especially in HTTP, have a best practice implementation however it is not necessary to adhere for connections/data to be established.

## Data Fields
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|url_original||string|The entirety of the URL combined together and or the URL in the truest form from the log source. Some log sources will already parse out portions of the URL into their respective fields. Other logs will even parse out the portions of the URL into their respective field but also include the "original" URL. Always try to include this field, because HTTP/URLs never truly have to conform to any RFC/implementation and thus any parsing/logging implementation could have any number of assumptions/mistakes - therefore it is best to keep a original value|ftp://BigwheelPassword:BigwheelBobUser@google.com:8088/common/Current/client/search/greatsearch.php?hash=215696fc36392ca70f89228b98060afb%20processname=example.exe#gid=l1k4h|
|url_category||string|The defined grouping of a URL (or could be just based on the domain in the URL) related to what it is (ie: adult, news, advertising, parked domains, etc)|Search Engines|
|url_host_name||string|The domain/host/hostname of the URL. This could be an IP address or any variation of a value but is more than likely a domain/hostname|google.com|
|url_extension||string|The extension (.dll, .php, zip, .msi, .txt, etc) without the "."|exe|
|url_fragment||string|The portion of the URL after the last "#", this is defined in https://tools.ietf.org/html/rfc3986#section-3.5. This is also referred to as the "hash" in some implementations. This value does not always exist|gid=l1k4h|
|url_path||string|Everything beginning with and after the first "/". This portion should usually exist in the log source / URL.. Even if the path is just "/". Also, even if the url_query or url_fragment have not been parsed yet then you still include them in this value|/common/Current/client/search/greatsearch.php?hash=215696fc36392ca70f89228b98060afb%20processname=example.exe|
|url_port||integer|The port in the URL. This is not to be confused with destination.md. In your ETL pipeline you should check if the value derived from the URL is actually an integer (unless properly verified in the data source)... because as mentioned throughout, URLs can be manipulated/mis-implemented in many different ways|8088|
|url_query||string|The portion of the URL beginning after the last "?" but not including the url fragment if it exists. This value does not always exist.|hash=215696fc36392ca70f89228b98060afb%20processname=example.exe|
|url_query_names||string|The keys/fields derived from the url_query. Due to the limitless variations of implementations of a URL, providing a nested object of key/values is not recommended. Whether an attacker is injecting data into a URL or an incorrect implementation or malicious implementation - it's possible you could have keys/fields of values of anything you can imagine (ie: "%*%)%*#Nf..$2f>hr..n fa.fa s\\\\\"\\jhrwq": "somevalue"|[ "215696fc36392ca70f89228b98060afb", "example.exe" ]|
|url_query_values||string|The values derived from the url_query. Due to the limitless variations of implementations of a URL, providing a nested object of key/values is not recommended. Whether an attacker is injecting data into a URL or an incorrect implementation or malicious implementation - it's possible you could have keys/fields of values of anything you can imagine (ie: "%*%)%*#Nf..$2f>hr..n fa.fa s\\\\\"\\jhrwq": "somevalue"|[ "hash" , "processname" ]|
|url_scheme||string|Defines the network location (ie: smtp, ftp, smb, ldap, etc). This portion may not exist in many log sources. The is usually the value that comes before the first "://". This is also referred to as URN/origin|ftp|
|url_user_password||string|The password defined in the URL. This is meant to be distinguished from something such as the value in the Authorization header in an HTTP request (or even the Proxy Authentication HTTP header)|BigwheelPassword|
|url_user_name||string|The username defined in the URL. This is meant to be distinguished from something such as the value in the Authorization header in an HTTP request (or even the Proxy Authentication HTTP header). This value should be copied to any.md|BigwheelBobUser|

## Resources
[HTTP](http.md)
[RFC-3986](https://tools.ietf.org/html/rfc3986#section-3.5)
