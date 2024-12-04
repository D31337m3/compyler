import psutil
import pytest
from compyler.core.compiler import Compiler

def test_memory_usage(temp_dir, sample_script):
    process = psutil.Process()
    initial_memory = process.memory_info().rss
    
    compiler = Compiler(sample_script, temp_dir)
    compiler.compile()
    
    peak_memory = process.memory_info().rss
    memory_increase = peak_memory - initial_memory
    
    # Ensure memory usage stays within reasonable bounds (100MB)
    assert memory_increase < 100 * 1024 * 1024
