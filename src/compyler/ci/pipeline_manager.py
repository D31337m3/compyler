class CIPipelineManager:
    def __init__(self):
        self.stages = {
            'build': self._build_stage,
            'test': self._test_stage,
            'validate': self._validation_stage,
            'package': self._package_stage,
            'deploy': self._deploy_stage
        }
        
    def run_pipeline(self):
        results = {}
        for stage_name, stage_func in self.stages.items():
            results[stage_name] = stage_func()
            if not results[stage_name]['success']:
                break
        return results
