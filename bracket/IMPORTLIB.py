# bracket/IMPORTLIB.py
# manage libraries importing

import sys

import rich

# [USE] [<lib>] → import <lib>
def USE_to_import(code: str):
    code = code.lstrip()
    keyword, lib = code.split(" ", 1)
    if keyword!="[USE]":
        raise SyntaxError(f"Expect `[USE]` got {keyword}")
    key = lib.removeprefix("[").removesuffix("]")
    dangerous_list = ['VAR', 'transpile', '__init__', 'LOOP', 'bkted', 'cli', 'IO', 'IMPORTLIB', 'BRANCH', 'FUN', 'CLASS', 'WARN', 'ERROR']
    if lib in dangerous_list:
        rich.print("[red]error:couldnot import built-in functions[/red]")
        sys.exit(1)
    return f"from bracket.{lib} import*"
