class PackageResolver:
    def __init__(self):
        self.dependency_graph = {}
        
    def resolve_requirements(self, requirements_file):
        with open(requirements_file) as f:
            for req in requirements.parse(f):
                self._add_requirement(req)
                
    def _add_requirement(self, requirement):
        dist = pkg_resources.working_set.find(
            pkg_resources.Requirement.parse(requirement.name)
        )
        if dist:
            self.dependency_graph[requirement.name] = {
                'version': dist.version,
                'dependencies': list(dist.requires())
            }
