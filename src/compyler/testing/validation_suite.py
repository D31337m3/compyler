class ValidationSuite:
    def __init__(self):
        self.validators = {
            'syntax': self._validate_syntax,
            'imports': self._validate_imports,
            'runtime': self._validate_runtime,
            'output': self._validate_output
        }
        
    def validate_compilation(self, source_file, output_file):
        results = {}
        for name, validator in self.validators.items():
            results[name] = validator(source_file, output_file)
        return results
