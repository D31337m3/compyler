from pathlib import Path
import inspect
import ast

class DocGenerator:
    def __init__(self, source_dir, output_dir="docs"):
        self.source_dir = Path(source_dir)
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        
    def generate_docs(self):
        # Generate API reference
        api_docs = self._generate_api_reference()
        self._write_markdown("api_reference.md", api_docs)
        
        # Generate usage examples
        examples = self._generate_examples()
        self._write_markdown("examples.md", examples)
        
        # Generate index
        self._generate_index()
