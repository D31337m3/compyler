from setuptools import setup, find_packages

setup(
    name='compyler',
    version='1.0.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'compyler=compyler.cli:main',
        ],
    },
    install_requires=[
        'psutil',
    ],
    python_requires='>=3.7',
)
