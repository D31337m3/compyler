class ArtifactManager:
    def __init__(self, artifact_dir="artifacts"):
        self.artifact_dir = Path(artifact_dir)
        self.artifact_dir.mkdir(exist_ok=True)
        
    def store_artifact(self, build_id, artifact_path):
        target_dir = self.artifact_dir / str(build_id)
        target_dir.mkdir(exist_ok=True)
        
        if isinstance(artifact_path, (str, Path)):
            shutil.copy2(artifact_path, target_dir)
        elif isinstance(artifact_path, dict):
            with open(target_dir / 'metadata.json', 'w') as f:
                json.dump(artifact_path, f, indent=2)
                
        return target_dir
