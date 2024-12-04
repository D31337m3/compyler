class CodeValidator:
    def __init__(self):
        self.security_rules = {
            'banned_imports': {'os.system', 'subprocess.call'},
            'unsafe_patterns': [r'eval\(', r'exec\('],
            'max_file_size': 10 * 1024 * 1024  # 10MB
        }
        
    def validate_source(self, source_file):
        with open(source_file) as f:
            content = f.read()
            
        violations = []
        violations.extend(self._check_imports(content))
        violations.extend(self._check_patterns(content))
        violations.extend(self._check_file_size(source_file))
        
        return violations
