class VersionControl:
    def __init__(self):
        self.versions = {}
        self.current_version = None
        
    def create_version(self, data):
        version_id = str(uuid.uuid4())
        timestamp = time.time()
        
        self.versions[version_id] = {
            'data': data,
            'timestamp': timestamp,
            'parent': self.current_version
        }
        
        self.current_version = version_id
        return version_id
