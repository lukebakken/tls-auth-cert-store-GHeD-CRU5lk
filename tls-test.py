import pika
import ssl

from pika.credentials import ExternalCredentials
from pika.credentials import PlainCredentials

context = ssl.create_default_context(cafile='./certs/ca_certificate.pem')
context.load_cert_chain('./certs/client_certificate.pem', './certs/client_key.pem')
ssl_options = pika.SSLOptions(context, 'shostakovich')

creds = ExternalCredentials()
# creds = PlainCredentials(username='guest', password='guest')

params = pika.ConnectionParameters(port=5671, ssl_options=ssl_options, credentials=creds)
connection = pika.BlockingConnection(params)
channel = connection.channel()
