class ResourceCleanup:
    def __init__(self):
        self.temp_files = set()
        self.temp_dirs = set()
        
    def register_temp_file(self, file_path):
        self.temp_files.add(Path(file_path))
        
    def register_temp_dir(self, dir_path):
        self.temp_dirs.add(Path(dir_path))
        
    def cleanup(self):
        for file_path in self.temp_files:
            if file_path.exists():
                file_path.unlink()
        
        for dir_path in self.temp_dirs:
            if dir_path.exists():
                shutil.rmtree(dir_path)
