import yaml
from pathlib import Path

class ConfigManager:
    DEFAULT_CONFIG = {
        'runtime': {
            'prefer_system_python': True,
            'embed_threshold_mb': 50,
        },
        'compilation': {
            'optimization_level': 1,
            'include_source_map': False,
        },
        'output': {
            'executable_format': 'native',
            'compression_level': 6,
        }
    }
    
    def __init__(self, config_file='compyler.yaml'):
        self.config_file = Path(config_file)
        self.config = self._load_config()