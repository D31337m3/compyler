
# Compyler - Python to Binary Compiler

A powerful tool that converts Python scripts into executable Linux binaries with zero dependencies.

## 🚀 Quick Start

```bash
git clone https://github.com/d31337m3/compyler.git

cd compyler

chmod +x compyler.py

🎯 Key Features
Zero external dependencies
Single binary output
Full Python functionality preservation
Automatic module handling
Native executable permissions
Linux system compatibility

📖 Usage
Basic Compilation

./compyler.py your_script.py

Quick Example
echo 'print("Hello World!")' > test.py

./compyler.py test.py

./test


🔬 Advanced Features

Self Compilation

./compyler.py compyler.py


Embedded Runtime
Bundles Python interpreter requirements
Includes necessary standard library modules
Handles dependencies resolution
Creates fully standalone executables
Reduces external Python version dependencies
Offline Mode
Works without network connectivity
Caches required modules locally
Preserves all imports during compilation
Creates air-gapped deployable binaries
Perfect for secure environments
Technical Specifications
Runtime Embedding
Automatically detects required Python modules
Packages core runtime components
Handles module search paths
Manages Python environment variables
Preserves sys.path modifications
Dependency Management
Static analysis of imports
Dynamic module resolution
Recursive dependency tracking
Standard library optimization
Custom module path support
Security Features
Integrity verification of compiled output
Checksum validation
Permission preservation
Source isolation
Runtime environment protection

Advanced Usage Examples

Custom Runtime Path

./compyler.py --runtime-path /custom/python/path script.py


Verbose Compilation

./compyler.py --verbose script.py


Module Inclusion

./compyler.py --include-modules module1,module2 script.py


Debug Mode

./compyler.py --debug script.py


🔧 Technical Architecture

Core Process
Bytecode Compilation: Python source → bytecode via py_compile
ZIP Packaging: Bytecode → ZIP archive
Binary Creation: Self-contained executable combining:
Python wrapper script
Compiled bytecode
ZIP archive
Key Components
PythonBinaryCompiler Class
Initialization with source path
Binary creation pipeline
ZIP data management
Permission handling

💼 Use Cases

Application Distribution
Single-file executable deployment
Simplified distribution
Portable applications
DevOps & System Tools
System administration scripts
Automation tools
Command-line utilities

📋 Requirements

Python 3.x
Linux operating system

⚠️ Current Limitations

Requires Python on target system
Linux-only support
Source code remains accessible

🛠️ Project Structure

compyler/
├── compyler.py        # Core compiler
├── README.md          # Documentation
└── LICENSE            # MIT License


🚀 Roadmap

Windows compatibility
Code obfuscation features
Custom binary naming
Multi-file compilation
Resource bundling
Cross-platform support

🤝 Contributing

We welcome contributions! Feel free to:
Report bugs
Suggest features
Submit pull requests
Improve documentation

📄 License

MIT License - See LICENSE file for details

🔗 Links

GitHub Repository
Issue Tracker
