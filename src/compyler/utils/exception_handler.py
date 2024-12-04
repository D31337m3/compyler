class CompylerException(Exception):
    def __init__(self, error_type, message=None, details=None):
        self.error_type = error_type
        self.message = message or error_type.value
        self.details = details
        super().__init__(self.message)

def handle_compiler_errors(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except CompylerException as e:
            logging.error(f"{e.error_type}: {e.message}")
            if e.details:
                logging.debug(f"Details: {e.details}")
            raise
        except Exception as e:
            logging.critical(f"Unexpected error: {str(e)}")
            logging.debug(f"Traceback: {traceback.format_exc()}")
            raise CompylerException(
                CompilerError.COMPILATION_FAILED,
                details=str(e)
            )
    return wrapper
