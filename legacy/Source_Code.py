from datetime import datetime
import ssl, socket, sys
from OpenSSL import SSL,crypto

print ("\n")
print ("""###############################################################
          SSL Certificate Fetch Tool - Power Of Python
###############################################################""")
print ("\n")

#Adding Disclaimer
print ("--------------------------------------------------------------------")
print ("------>  DISCLAIMER : ")
print ("This Program is to fetch the SSL certificate from a Server")
print ("This Program does not make any changes to any Server Configuration")
print ("It is free software and it comes without any Warranty")
print ("--------------------------------------------------------------------")
print ("\n")

host = 'google.co.in'
cert = ''
ssl_version = ssl.PROTOCOL_TLSv1

if (len(sys.argv) > 1):
  host = sys.argv[1]

try:
   cert=ssl.get_server_certificate((host, 443), ssl_version)
#   print ("The Certificate is %s") % (cert)
except Exception as e:
   print ("Could not connect error !! Error is %s") % (e)
   print ("\n\n")

if (cert):
 # OpenSSL
 x509 = crypto.load_certificate(crypto.FILETYPE_PEM, cert)
 print ("--> Connecting to Remote host: %s") % (host)
 print ("\n")
 print ("* The Certificate version is           : %s" ) % (x509.get_version())
 print ("* The Certificate Issuer is            : %s" ) % (x509.get_issuer().get_components())
 print ("* The Certificate Algorithm is         : %s" ) % (x509.get_signature_algorithm())
 print ("* The Certificate Paramters are        : %s" ) % (x509.get_subject().get_components())
 print ("* The Certificate Public Key Length is : %d") % (x509.get_pubkey().bits())
 time = x509.get_notBefore()
 print ("* The Certificate Validity is from     : Date - %s ; Time - %s") % (time[:8],time[8:])
 time = x509.get_notAfter()
 print ("* The Certificate Validity is upto     : Date - %s ; Time - %s") % (time[:8],time[8:])
 print ("\n\n")
 print ("-> End !")
 print ("\n")
