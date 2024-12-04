import hashlib
import hmac
import base64

class SecurityValidator:
    def __init__(self, secret_key=b'compyler-key'):
        self.secret_key = secret_key
    
    def sign_code(self, code_bytes):
        signature = hmac.new(self.secret_key, code_bytes, hashlib.sha256)
        return base64.b64encode(signature.digest())
    
    def verify_signature(self, code_bytes, signature):
        computed_sig = self.sign_code(code_bytes)
        return hmac.compare_digest(computed_sig, signature)
