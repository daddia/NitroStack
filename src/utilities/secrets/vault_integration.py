import hvac
import os

VAULT_ADDR = os.getenv("VAULT_ADDR")
VAULT_TOKEN = os.getenv("VAULT_TOKEN")

client = hvac.Client(url=VAULT_ADDR, token=VAULT_TOKEN)

def get_secret(secret_path):
    if client.is_authenticated():
        secret = client.secrets.kv.read_secret_version(path=secret_path)
        return secret['data']['data']
    else:
        raise Exception("Vault authentication failed")
