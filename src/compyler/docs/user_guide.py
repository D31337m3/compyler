class UserGuideGenerator:
    SECTIONS = [
        'getting_started',
        'basic_usage',
        'advanced_features',
        'troubleshooting',
        'best_practices'
    ]
    
    def generate_guide(self):
        guide = ["# Compyler User Guide\n"]
        
        for section in self.SECTIONS:
            content = getattr(self, f'_generate_{section}')()
            guide.extend(content)
            
        return '\n'.join(guide)
        
    def _generate_getting_started(self):
        return [
            "## Getting Started\n",
            "### Installation\n",
            "\npip install compyler\n\n",
            "### Quick Start\n",
            "\ncompyler your_script.py\n\n"
        ]
