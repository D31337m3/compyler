class EnvironmentManager:
    def __init__(self):
        self.env_prefix = 'COMPYLER_'
        self.environment = self._load_environment()
        
    def get_setting(self, key, default=None):
        env_key = f"{self.env_prefix}{key.upper()}"
        return os.getenv(env_key, default)
        
    def set_setting(self, key, value):
        env_key = f"{self.env_prefix}{key.upper()}"
        os.environ[env_key] = str(value)
