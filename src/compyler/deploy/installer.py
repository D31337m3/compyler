class InstallerBuilder:
    INSTALLER_TEMPLATE = """
#!/bin/bash
# Installer script for {app_name}

INSTALL_DIR="/usr/local/bin"
APP_NAME="{app_name}"

echo "Installing {app_name} v{version}..."
mkdir -p $INSTALL_DIR
cp bin/* $INSTALL_DIR/
chmod +x $INSTALL_DIR/$APP_NAME

echo "Installation complete!"
"""
    
    def build_installer(self, dist_path, app_name, version):
        installer_path = dist_path / f"install_{app_name}.sh"
        with open(installer_path, 'w') as f:
            f.write(self.INSTALLER_TEMPLATE.format(
                app_name=app_name,
                version=version
            ))
        os.chmod(installer_path, 0o755)
