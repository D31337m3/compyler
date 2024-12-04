class ReleaseManager:
    def __init__(self):
        self.releases = []
        self.current_release = None
        
    def create_release(self, version, artifacts):
        release = {
            'version': version,
            'artifacts': artifacts,
            'timestamp': time.time(),
            'changelog': self._generate_changelog(),
            'status': 'pending'
        }
        
        self.releases.append(release)
        return release
