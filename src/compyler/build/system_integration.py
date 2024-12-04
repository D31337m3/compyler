from pathlib import Path
import subprocess

class BuildSystemIntegrator:
    def __init__(self, project_root):
        self.project_root = Path(project_root)
        
    def generate_cmake_config(self):
        cmake_template = """
cmake_minimum_required(VERSION 3.10)
project(CompiledPythonProject)

add_custom_target(compile_python
    COMMAND compyler ${SOURCE_FILES}
    WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
)
"""
        with open(self.project_root / "CMakeLists.txt", "w") as f:
            f.write(cmake_template)
