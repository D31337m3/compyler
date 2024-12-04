class AuthorizationManager:
    def __init__(self):
        self.permissions = {
            'admin': ['read', 'write', 'execute', 'manage'],
            'developer': ['read', 'write', 'execute'],
            'user': ['read', 'execute']
        }
        
    def check_permission(self, user, required_permission):
        user_role = user.get('role', 'user')
        allowed_permissions = self.permissions.get(user_role, [])
        return required_permission in allowed_permissions
