class AuthenticationManager:
    def __init__(self):
        self.token_store = {}
        self.secret_key = os.getenv('JWT_SECRET_KEY')
        
    def authenticate_user(self, credentials):
        user = self._verify_credentials(credentials)
        if user:
            token = self._generate_token(user)
            self.token_store[token] = user
            return token
            
    def _verify_token(self, token):
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=['HS256'])
            return payload
        except jwt.InvalidTokenError:
            return None
