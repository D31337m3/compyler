import logging
import traceback
from enum import Enum

class CompilerError(Enum):
    RUNTIME_NOT_FOUND = "Python runtime not found"
    COMPILATION_FAILED = "Compilation failed"
    PACKAGING_FAILED = "Packaging failed"
    INVALID_SOURCE = "Invalid source file"

class ErrorHandler:
    def __init__(self):
        self.logger = logging.getLogger('compyler')
        self._setup_logging()
        
    def _setup_logging(self):
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handler = logging.StreamHandler()
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
