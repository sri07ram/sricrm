import secrets
from knox.models import AuthToken

def generate_custom_token_string():
    return secrets.token_hex(64)

AuthToken.generate_token_string = staticmethod(generate_custom_token_string)
