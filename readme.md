
# Compyler - Python to Binary Compiler

A lightweight, dependency-free tool that converts Python scripts into executable Linux binaries.

## Features

- Creates standalone executable binaries from Python scripts
- No external dependencies required
- Preserves all original script functionality
- Handles Python imports and modules
- Maintains executable permissions
- Works on any Linux system with Python installed

## Installation

Clone the repository:
```bash
git clone https://github.com/d31337m3/compyler.git
cd compyler
chmod +x compylersrc.py
Usage
Basic compilation:

./compylersrc.py your_script.py

Copy

Execute

This creates an executable binary with the same name as your script (without the .py extension).

Example:

# Create a test script
echo 'print("Hello World!")' > test.py

# Compile it
./compylersrc.py test.py

# Run the binary
./test

Copy

Execute

How It Works
Bytecode Compilation: Converts Python source to bytecode using py_compile
ZIP Packaging: Packages the bytecode into a ZIP archive
Binary Creation: Creates a self-contained executable combining:
Python wrapper script
Compiled bytecode
ZIP archive
Technical Details
Core Components
PythonBinaryCompiler class:
__init__: Initializes compiler with source file path
create_binary: Handles the compilation process
Key Functions
find_zip_start(): Locates ZIP data in binary
main(): Entry point and argument handling
Temporary directory management for compilation
Executable permission setting
Use Cases
Application Distribution

Package Python apps as single executables
Simplify deployment processes
Command Line Tools

Convert Python scripts to system commands
Create portable utilities
System Integration

Package scripts for system administration
Create executable tools for automation
Requirements
Python 3.x
Linux-based operating system
Limitations
Target system must have Python installed
Linux systems only
Source code remains accessible (not obfuscated)
Contributing
Contributions welcome! Feel free to:

Submit bug reports
Propose new features
Create pull requests
License
MIT License - See LICENSE file for details

Project Structure
compyler/
├── compylersrc.py     # Main compiler source
├── README.md          # Documentation
└── LICENSE            # License file

Copy

Execute

Future Enhancements
Windows support
Code obfuscation options
Custom binary naming
Multiple file compilation
Resource bundling
