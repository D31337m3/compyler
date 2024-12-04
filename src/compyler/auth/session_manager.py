class SessionManager:
    def __init__(self):
        self.sessions = {}
        self.session_duration = timedelta(hours=24)
        
    def create_session(self, user_id):
        session_id = str(uuid.uuid4())
        session = {
            'user_id': user_id,
            'created_at': datetime.now(),
            'expires_at': datetime.now() + self.session_duration,
            'active': True
        }
        self.sessions[session_id] = session
        return session_id
