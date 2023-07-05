import os
import secrets


class FlaskConfig(object):
    def __init__(self):
        self.SECRET_KEY = self.get_secret_key()
        self.DEBUG = os.getenv("FLASK_DEBUG", "False") == "True"

    def get_secret_key(self):
        token = secrets.token_hex()
        return token.encode()

    def __str__(self):
        return f"SECRET_KEY={self.SECRET_KEY[:5]}..., DEBUG={self.DEBUG}"
