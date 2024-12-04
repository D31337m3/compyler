class RollbackManager:
    def __init__(self, backup_dir="backups"):
        self.backup_dir = Path(backup_dir)
        self.backup_dir.mkdir(exist_ok=True)
        
    def create_backup(self, deployment):
        backup = {
            'deployment_id': deployment['id'],
            'timestamp': time.time(),
            'files': self._backup_files(deployment)
        }
        return backup
        
    def rollback(self, deployment_id):
        backup = self._find_backup(deployment_id)
        if backup:
            self._restore_backup(backup)
            return True
        return False
