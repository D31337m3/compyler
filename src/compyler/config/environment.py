class EnvironmentManager:
    ENV_PREFIX = 'COMPYLER_'
    
    def __init__(self):
        self.env_vars = self._load_environment()
        
    def _load_environment(self):
        return {
            key[len(self.ENV_PREFIX):].lower(): value
            for key, value in os.environ.items()
            if key.startswith(self.ENV_PREFIX)
        }
        
    def get_setting(self, key, default=None):
        env_key = f"{self.ENV_PREFIX}{key.upper()}"
        return os.getenv(env_key, default)
