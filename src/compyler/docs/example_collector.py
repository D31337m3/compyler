class ExampleCollector:
    def collect_examples(self, examples_dir):
        examples = []
        for example_file in Path(examples_dir).glob('*.py'):
            with open(example_file) as f:
                content = f.read()
                tree = ast.parse(content)
                docstring = ast.get_docstring(tree)
                
                examples.append({
                    'title': example_file.stem,
                    'description': docstring,
                    'code': content
                })
        
        return examples
