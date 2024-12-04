import os
import subprocess
from pathlib import Path
import pytest
from compyler.core.compiler import Compiler

def test_compile_and_run(temp_dir, sample_script):
    # Full compilation test
    compiler = Compiler(sample_script, temp_dir)
    exe_path = compiler.compile()
    
    # Run the compiled executable
    result = subprocess.run([str(exe_path)], 
                          capture_output=True, 
                          text=True)
    
    assert result.returncode == 0
    assert "Test Script" in result.stdout
