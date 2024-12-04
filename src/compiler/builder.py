import os
import shutil
import py_compile
import stat
import importlib
import pkgutil

class BinaryBuilder:
    def __init__(self, output_dir='dist'):
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
    
    def build(self, source_file):
        # Create single output executable
        output_path = os.path.join(self.output_dir, 
            os.path.splitext(os.path.basename(source_file))[0])
        
        with open(output_path, 'w') as f:
            # Add shebang
            f.write('#!/usr/bin/env python3\n\n')
            
            # Bundle all compiler modules
            for module in ['threading', 'cache', 'monitor', 'security', 
                         'distributed', 'discovery', 'optimizer', 'builder']:
                module_path = f'src/compiler/{module}.py'
                if os.path.exists(module_path):
                    with open(module_path) as mod:
                        f.write(f'# {module}.py\n')
                        f.write(mod.read())
                        f.write('\n\n')
            
            # Add main code
            with open(source_file) as src:
                f.write('# main.py\n')
                f.write(src.read())
        
        # Make executable
        os.chmod(output_path, os.stat(output_path).st_mode | stat.S_IEXEC)
        return output_path