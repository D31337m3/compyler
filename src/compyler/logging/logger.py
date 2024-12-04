class CompylerLogger:
    def __init__(self, log_dir="logs"):
        self.log_dir = Path(log_dir)
        self.log_dir.mkdir(exist_ok=True)
        self.loggers = {
            'compilation': self._setup_logger('compilation'),
            'performance': self._setup_logger('performance'),
            'security': self._setup_logger('security')
        }
        
    def _setup_logger(self, name):
        logger = logging.getLogger(f'compyler.{name}')
        handler = RotatingFileHandler(
            self.log_dir / f'{name}.log',
            maxBytes=10*1024*1024,  # 10MB
            backupCount=5
        )
        handler.setFormatter(self._get_formatter())
        logger.addHandler(handler)
        return logger
