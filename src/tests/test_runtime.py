import unittest
from compyler.runtime.loader import RuntimeLoader
from compyler.utils.memory_manager import RuntimeManager

class TestRuntime(unittest.TestCase):
    def test_runtime_detection(self):
        with RuntimeManager() as rm:
            loader = RuntimeLoader()
            runtime = loader.get_runtime()
            self.assertIsNotNone(runtime)
            
    def test_embedded_runtime(self):
        with RuntimeManager() as rm:
            loader = RuntimeLoader()
            runtime = loader.get_runtime(embed_runtime=True)
            self.assertIsNotNone(runtime)
