class ProfileManager:
    def __init__(self, profiles_dir="profiles"):
        self.profiles_dir = Path(profiles_dir)
        self.profiles_dir.mkdir(exist_ok=True)
        self.active_profile = None
        
    def load_profile(self, profile_name):
        profile_path = self.profiles_dir / f"{profile_name}.yaml"
        if profile_path.exists():
            with open(profile_path) as f:
                self.active_profile = yaml.safe_load(f)
                return self.active_profile
