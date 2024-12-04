import argparse
import sys
from pathlib import Path
from .core.compiler import Compiler

def create_parser():
    parser = argparse.ArgumentParser(
        description='Compyler - Python to Executable Compiler'
    )
    parser.add_argument(
        'source',
        help='Source Python file to compile'
    )
    parser.add_argument(
        '-o', '--output',
        help='Output directory for executable',
        default=None
    )
    parser.add_argument(
        '--embed-runtime',
        action='store_true',
        help='Force embedding Python runtime'
    )
    return parser

def main():
    parser = create_parser()
    args = parser.parse_args()
    
    compiler = Compiler(args.source, args.output)
    compiler.compile(embed_runtime=args.embed_runtime)
