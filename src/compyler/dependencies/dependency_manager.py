from pathlib import Path
import pkg_resources
import requirements

class DependencyManager:
    def __init__(self, project_root):
        self.project_root = Path(project_root)
        self.requirements_file = self.project_root / 'requirements.txt'
        
    def analyze_dependencies(self, source_file):
        imports = self._extract_imports(source_file)
        dependencies = self._resolve_dependencies(imports)
        return dependencies
        
    def _extract_imports(self, source_file):
        with open(source_file) as f:
            tree = ast.parse(f.read())
        return {node.names[0].name 
                for node in ast.walk(tree) 
                if isinstance(node, ast.Import)}
