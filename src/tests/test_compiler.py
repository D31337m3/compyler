import unittest
import tempfile
import os
from pathlib import Path
from compyler.core.compiler import Compiler

class TestCompiler(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        self.test_file = Path(self.test_dir) / "test_script.py"
        with open(self.test_file, "w") as f:
            f.write("print('Hello, World!')")
            
    def test_basic_compilation(self):
        compiler = Compiler(self.test_file)
        result = compiler.compile()
        self.assertTrue(result.exists())
        self.assertTrue(result.stat().st_size > 0)
