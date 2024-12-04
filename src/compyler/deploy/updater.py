class AutoUpdater:
    def __init__(self, current_version):
        self.current_version = current_version
        
    def check_for_updates(self, update_url):
        # Check latest version
        latest_version = self._fetch_latest_version(update_url)
        return latest_version > self.current_version
        
    def update(self, update_url):
        if self.check_for_updates(update_url):
            self._download_update(update_url)
            self._apply_update()
            return True
        return False
