import mysql.connector
from dotenv import load_dotenv
import os
import base64

load_dotenv()

def get_connection():
# Ensure the certs directory exists
    os.makedirs("certs", exist_ok=True)

    # Decode the CA certificate from environment variable
    cert_path = "certs/ca.pem"
    if not os.path.exists(cert_path):
        b64_cert = os.environ.get("CA_CERT_B64")
        if b64_cert:
            with open(cert_path, "wb") as cert_file:
                cert_file.write(base64.b64decode(b64_cert))
        else:
            raise ValueError("CA_CERT_B64 environment variable is missing")

    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASS"),
        database=os.getenv("DB"),
        port=os.getenv("DB_PORT"),
        ssl_ca=os.getenv("DB_CA")
    )
