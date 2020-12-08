from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography import x509
from cryptography.x509.oid import NameOID

import datetime

# script to generate a private key and self signed certificate for the server

key = rsa.generate_private_key(public_exponent=65537, key_size=2048, backend=default_backend())

with open('server-key.pem', 'wb') as f:
    f.write(key.private_bytes(encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.TraditionalOpenSSL,
    encryption_algorithm=serialization.BestAvailableEncryption(b'passphrase'),
    ))

subject = issuer = x509.Name([x509.NameAttribute(NameOID.ORGANIZATION_NAME, u'home')])

cert = x509.CertificateBuilder().subject_name(subject).issuer_name(issuer).public_key(key.public_key()
    ).serial_number(x509.random_serial_number()).not_valid_before(datetime.datetime.utcnow()
    ).not_valid_after(datetime.datetime.utcnow() + datetime.timedelta(days=365)
    ).add_extension(x509.SubjectAlternativeName([x509.DNSName(u'localhost')]), critical=False,).sign(key, hashes.SHA256(), default_backend())

with open('server-certificate.pem', 'wb') as f:
    f.write(cert.public_bytes(serialization.Encoding.PEM))