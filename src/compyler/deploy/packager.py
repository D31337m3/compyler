import shutil
import os
from pathlib import Path

class Packager:
    def __init__(self, build_dir, dist_dir="dist"):
        self.build_dir = Path(build_dir)
        self.dist_dir = Path(dist_dir)
        
    def create_distribution(self, app_name, version):
        dist_path = self.dist_dir / f"{app_name}-{version}"
        os.makedirs(dist_path, exist_ok=True)
        
        # Copy executables
        self._copy_executables(dist_path)
        # Copy dependencies
        self._copy_dependencies(dist_path)
        # Generate metadata
        self._generate_metadata(dist_path, app_name, version)
        
        return self._create_archive(dist_path)
