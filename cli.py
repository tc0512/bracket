#!/usr/bin/env python3
# bracket/cli.py
# CLI entertainment of bracket-lang

import sys
import argparse
from .transpile import transpile

def main():
    parser = argparse.ArgumentParser(
        prog="bracket",
        description="bracket-lang transpiler",
        epilog="for example: bracket run main.bracket"
    )
    subparsers = parser.add_subparsers(dest="command", required=True)
    # run command
    run_parser = subparsers.add_parser("run", help="run .bracket file")
    run_parser.add_argument("file", help="the .bracket file you want to run")
    # build command
    build_parser = subparsers.add_parser("build", help="transpile .bracket file to .py")
    build_parser.add_argument("file", help="the .bracket file you want to transpile")
    build_parser.add_argument("-o", "--output", help="output file name(default same name .py)")
    args = parser.parse_args()
    if args.command == "run":
        with open(args.file, "r", encoding="utf-8") as f:
            code = f.read()
        py_code = transpile(code)
        exec(py_code)
    elif args.command == "build":
        with open(args.file, "r", encoding="utf-8") as f:
            code = f.read()
        py_code = transpile(code)
        output = args.output or args.file.replace(".bracket", ".py")
        with open(output, "w", encoding="utf-8") as f:
            f.write(py_code)
        print(f"✓ transpile finished: {output}")

if __name__ == "__main__":
    main()
