class StorageManager:
    def __init__(self, storage_dir="storage"):
        self.storage_dir = Path(storage_dir)
        self.storage_dir.mkdir(exist_ok=True)
        
    def store_binary(self, binary_data, identifier):
        file_path = self.storage_dir / f"{identifier}.bin"
        with open(file_path, 'wb') as f:
            f.write(binary_data)
        return file_path
