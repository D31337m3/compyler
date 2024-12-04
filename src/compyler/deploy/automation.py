class DeploymentAutomator:
    def __init__(self, config_file="deploy_config.yaml"):
        self.config = self._load_config(config_file)
        self.environments = ['dev', 'staging', 'prod']
        
    def deploy(self, artifact_path, environment):
        if environment not in self.environments:
            raise ValueError(f"Invalid environment: {environment}")
            
        deployment = {
            'artifact': artifact_path,
            'environment': environment,
            'timestamp': time.time(),
            'status': 'pending'
        }
        
        try:
            self._run_deployment_steps(deployment)
            deployment['status'] = 'success'
        except Exception as e:
            deployment['status'] = 'failed'
            deployment['error'] = str(e)
