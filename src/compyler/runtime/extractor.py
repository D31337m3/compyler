import zipfile
import os

class RuntimeExtractor:
    def __init__(self, runtime_manager):
        self.rm = runtime_manager
        
    def extract_runtime(self, zip_path, chunk_size=8192):
        temp_dir = self.rm.create_temp_dir()
        
        with zipfile.ZipFile(zip_path) as zf:
            for item in zf.filelist:
                target_path = os.path.join(temp_dir, item.filename)
                os.makedirs(os.path.dirname(target_path), exist_ok=True)
                
                with zf.open(item) as source, open(target_path, 'wb') as target:
                    while True:
                        chunk = source.read(chunk_size)
                        if not chunk:
                            break
                        target.write(chunk)
                        del chunk
                        
        return temp_dir
