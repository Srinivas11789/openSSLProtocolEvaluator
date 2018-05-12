# Module import
from datetime import datetime
import ssl, socket, sys
from OpenSSL import SSL,crypto


class ssl_connect:

    def __init__(self, host, ssl_version=ssl.PROTOCOL_TLSv1):
        self.host = host
        self.ssl_version = ssl_version

    def default_certificate_fetch(self):
        cert = ''

        try:
            cert = ssl.get_server_certificate((self.host, 443), self.ssl_version)
        except Exception as e:
            print ("Could not connect error !! Error is %s") % (e)

        certificate = {}

        if (cert):
            x509 = crypto.load_certificate(crypto.FILETYPE_PEM, cert)
            certificate.update({"host":self.host})
            certificate.update({"version":x509.get_version()})
            certificate.update({"issuer":x509.get_issuer().get_components()})
            certificate.update({"signature_algorithm":x509.get_signature_algorithm()})
            certificate.update({"parameters": x509.get_subject().get_components()})
            certificate.update({"key_length":x509.get_pubkey().bits()})
            time = x509.get_notBefore()
            certificate.update({"validity_start":time[:8]+time[8:]})
            time = x509.get_notAfter()
            certificate.update({"validity_end":time[:8]+time[8:]})

        return certificate

    def crypto_supported(self):
        # Key exchange cryptography - cipher list
        pass

    def ssl_support(self):
        # Depreceiation Attack
        pass


def main():
    sslconnection = ssl_connect("google.co.in")
    print sslconnection.default_certificate_fetch()

main()
