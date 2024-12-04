def process_large_files(directory):
    def file_generator(dir_path):
        for root, _, files in os.walk(dir_path):
            for file in files:
                yield os.path.join(root, file)
    
    for file_path in file_generator(directory):
        process_single_file(file_path)
        gc.collect()  # Force garbage collection after each file

def process_single_file(file_path, buffer_size=8192):
    with open(file_path, 'rb') as f:
        while True:
            buffer = f.read(buffer_size)
            if not buffer:
                break
            # Process buffer
            del buffer  # Explicit cleanup
