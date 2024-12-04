class CompilerTestRunner:
    def __init__(self, test_dir="tests"):
        self.test_dir = Path(test_dir)
        self.results = []
        
    def run_test_suite(self):
        test_files = self.test_dir.glob("**/*.py")
        for test_file in test_files:
            result = self._run_single_test(test_file)
            self.results.append(result)
            
    def _run_single_test(self, test_file):
        start_time = time.time()
        try:
            self._compile_and_validate(test_file)
            status = "PASS"
        except Exception as e:
            status = "FAIL"
            error = str(e)
