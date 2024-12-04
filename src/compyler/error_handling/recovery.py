class RecoveryManager:
    def __init__(self):
        self.recovery_strategies = {
            'compilation': self._recover_compilation,
            'memory': self._recover_memory,
            'filesystem': self._recover_filesystem
        }
        
    def attempt_recovery(self, error_context):
        strategy = self.recovery_strategies.get(error_context['type'])
        if strategy:
            return strategy(error_context)
        return False
