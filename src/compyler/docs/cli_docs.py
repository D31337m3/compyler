class CLIDocumentationGenerator:
    def __init__(self):
        self.commands = []
        self.examples = []
        
    def add_command(self, name, description, usage, options=None):
        self.commands.append({
            'name': name,
            'description': description,
            'usage': usage,
            'options': options or []
        })
        
    def generate_cli_docs(self):
        doc = ["# Compyler CLI Reference\n"]
        
        # Generate command reference
        doc.append("## Commands\n")
        for cmd in self.commands:
            doc.extend([
                f"### {cmd['name']}\n",
                f"{cmd['description']}\n",
                "#### Usage:\n",
                f"\n{cmd['usage']}\n\n"
            ])
