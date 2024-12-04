class ErrorManager:
    def __init__(self):
        self.error_handlers = {
            CompilationError: self._handle_compilation_error,
            RuntimeError: self._handle_runtime_error,
            MemoryError: self._handle_memory_error
        }
        self.error_log = []
        
    def handle_error(self, error):
        error_type = type(error)
        handler = self.error_handlers.get(error_type, self._handle_generic_error)
        return handler(error)
        
    def _log_error(self, error, context):
        self.error_log.append({
            'timestamp': time.time(),
            'error_type': type(error).__name__,
            'message': str(error),
            'context': context
        })
