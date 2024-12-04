class APIReferenceBuilder:
    def build_reference(self, module):
        reference = []
        
        for name, obj in inspect.getmembers(module):
            if inspect.isclass(obj):
                reference.extend(self._document_class(obj))
            elif inspect.isfunction(obj):
                reference.extend(self._document_function(obj))
                
        return '\n'.join(reference)
        
    def _document_class(self, cls):
        docs = [f"## {cls.__name__}\n"]
        docs.append(inspect.getdoc(cls) or "No description available.")
        
        # Document methods
        for name, method in inspect.getmembers(cls, inspect.isfunction):
            if not name.startswith('_'):
                docs.extend(self._document_function(method, indent=True))
                
        return docs
