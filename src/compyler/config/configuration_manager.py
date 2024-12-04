class ConfigurationManager:
    def __init__(self, config_file="config.yaml"):
        self.config_file = Path(config_file)
        self.config = self._load_config()
        self.watchers = []
        
    def _load_config(self):
        if self.config_file.exists():
            with open(self.config_file) as f:
                return yaml.safe_load(f)
        return self._get_default_config()
        
    def watch_config(self, callback):
        self.watchers.append(callback)
