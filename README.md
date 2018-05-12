
### Legacy Feature and Tool

### OpenSSL-Certificate-Fetcher: 
          Fetches the SSL Certificate of the remote server and displays the details

#### Example Output:

```
[root@server5 pandian]# python openssl1.py "paytm.com"


###############################################################
          SSL Certificate Fetch Tool - Power Of Python
###############################################################


--------------------------------------------------------------------
------>  DISCLAIMER :
This Program is to fetch the SSL certificate from a Server
This Program does not make any changes to any Server Configuration
It is free software and it comes without any Warranty
--------------------------------------------------------------------


--> Connecting to Remote host: paytm.com


* The Certificate version is           : 2
* The Certificate Issuer is            : [('C', 'US'), ('O', 'GeoTrust Inc.'), ('CN', 'GeoTrust SSL CA - G3')]
* The Certificate Algorithm is         : sha256WithRSAEncryption
* The Certificate Paramters are        : [('C', 'IN'), ('ST', 'Delhi'), ('L', 'New Delhi'), ('O', 'One97 Communications Ltd.'), ('CN', '*.paytm.com')]
* The Certificate Public Key Length is : 2048
* The Certificate Validity is from     : Date - 20151013 ; Time - 000000Z
* The Certificate Validity is upto     : Date - 20170826 ; Time - 235959Z



-> End !


[root@server5 pandian]# python openssl1.py "amazon.com"


###############################################################
          SSL Certificate Fetch Tool - Power Of Python
###############################################################


--------------------------------------------------------------------
------>  DISCLAIMER :
This Program is to fetch the SSL certificate from a Server
This Program does not make any changes to any Server Configuration
It is free software and it comes without any Warranty
--------------------------------------------------------------------


--> Connecting to Remote host: amazon.com


* The Certificate version is           : 2
* The Certificate Issuer is            : [('C', 'US'), ('O', 'Symantec Corporation'), ('OU', 'Symantec Trust Network'), ('CN', 'Symantec Class 3 Secure Server CA - G4')]
* The Certificate Algorithm is         : sha256WithRSAEncryption
* The Certificate Paramters are        : [('C', 'US'), ('ST', 'Washington'), ('L', 'Seattle'), ('O', 'Amazon.com, Inc.'), ('CN', 'www.amazon.com')]
* The Certificate Public Key Length is : 2048
* The Certificate Validity is from     : Date - 20160518 ; Time - 000000Z
* The Certificate Validity is upto     : Date - 20161230 ; Time - 235959Z



-> End !
```

