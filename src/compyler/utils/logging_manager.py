import logging
import sys
from pathlib import Path

class LoggingManager:
    def __init__(self, log_dir="logs"):
        self.log_dir = Path(log_dir)
        self.log_dir.mkdir(exist_ok=True)
        
    def setup_logging(self, level=logging.INFO):
        # File handler
        file_handler = logging.FileHandler(
            self.log_dir / "compyler.log"
        )
        file_handler.setLevel(logging.DEBUG)
        
        # Console handler
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(level)
        
        # Configure root logger
        logging.basicConfig(
            level=logging.DEBUG,
            handlers=[file_handler, console_handler],
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
