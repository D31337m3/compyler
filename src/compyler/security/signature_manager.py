import hashlib
import hmac
from cryptography.fernet import Fernet

class SignatureManager:
    def __init__(self, key_file='signing_key.key'):
        self.key_file = key_file
        self.key = self._load_or_generate_key()
        
    def sign_executable(self, executable_path):
        with open(executable_path, 'rb') as f:
            content = f.read()
            
        signature = hmac.new(
            self.key,
            content,
            hashlib.sha256
        ).hexdigest()
        
        return signature
