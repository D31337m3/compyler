class PluginHooks:
    def __init__(self):
        self.pre_compile_hooks = []
        self.post_compile_hooks = []
        self.build_hooks = []
        
    def register_hook(self, hook_type, callback):
        if hook_type == 'pre_compile':
            self.pre_compile_hooks.append(callback)
        elif hook_type == 'post_compile':
            self.post_compile_hooks.append(callback)
        elif hook_type == 'build':
            self.build_hooks.append(callback)
            
    def run_hooks(self, hook_type, *args, **kwargs):
        hooks = getattr(self, f'{hook_type}_hooks', [])
        results = []
        for hook in hooks:
            results.append(hook(*args, **kwargs))
        return results
