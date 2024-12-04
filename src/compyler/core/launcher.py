class Launcher:
    def __init__(self):
        self.launcher_template = """
import sys
import os
import runpy

def main():
    sys.path.insert(0, os.path.dirname(__file__))
    runpy.run_path(sys.argv[1], run_name='__main__')

if __name__ == '__main__':
    main()
"""
    
    def generate_launcher(self, output_path):
        with open(output_path, 'w') as f:
            f.write(self.launcher_template)
