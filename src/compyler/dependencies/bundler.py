class DependencyBundler:
    def __init__(self, output_dir):
        self.output_dir = Path(output_dir)
        
    def bundle_dependencies(self, dependencies):
        bundle_dir = self.output_dir / 'lib'
        bundle_dir.mkdir(exist_ok=True)
        
        for package_name, package_info in dependencies.items():
            self._copy_package(package_name, bundle_dir)
            
    def _copy_package(self, package_name, target_dir):
        dist = pkg_resources.working_set.find(
            pkg_resources.Requirement.parse(package_name)
        )
        if dist:
            package_path = Path(dist.location)
            if package_path.is_dir():
                shutil.copytree(
                    package_path,
                    target_dir / package_name,
                    ignore=shutil.ignore_patterns('*.pyc', '__pycache__')
                )
