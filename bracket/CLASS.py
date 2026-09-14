#!/usr/bin/env python3
# bracket/CLASS.py
# manage classes defining

import sys
from keyword import kwlist

import rich

# [CLASS] [<class name>] [<parent class>] → class <class name>(<parent class>):
def CLASS_to_class(code: str):
    code = code.lstrip()
    keyword, rest = code.split(" ", 1)
    if keyword!="[CLASS]":
        rich.print(f"[red]{code}[/red]")
        rich.print(f"[red]Expected `CLASS` got `{keyword}`.[/red]")
        sys.exit(1)
    inner = rest.removeprefix("[").removesuffix("]")
    parts = inner.split("] [")
    if len(parts) != 2:
        rich.print(f"[red]{code}[/red]")
        rich.print("[red]error:Something wrong in your code")
        rich.print("[red]The usage of `[CLASS]` sentences is `[CLASS] [<class name>] [<parent class>]`[/red]")
        sys.exit(1)
    class_name = parts[0].strip()
    parent_class = parts[1].strip()
    if not class_name:
        rich.print(f"[red]{code}[/red]")
        rich.print("[red]error:Class name cannot be empty.[/red]")
        sys.exit(1)
    dangerous_list = kwlist+["INFO", "VAR", "INPUT", "IF", "ELSEIF", "ELSE", "FOR", "WHILE", "LOOP", "FUNC", "CLASS", "ERROR", "WARN", "USE"]
    if not class_name.isidentifier():
        rich.print(f"[red]{code}[/red]")
        rich.print(f"[red]error:Invalid class name: {class_name}.[/red]")
        sys.exit(1)
    if class_name in dangerous_list:
        rich.print(f"[red]{code}[/red]")
        rich.print(f"[red]error:Invalid class name: {class_name}.[/red]")
        sys.exit(1)
    return f"class {class_name}({parent_class}):"

def transpile_line(line: str) -> str:
    """transpile one line of bracket code and operate indents"""
    indent = len(line) - len(line.lstrip())
    stripped = line.lstrip()
    if not stripped:
        return ""
    if stripped.startswith("[CLASS]"):
        return " " * indent + CLASS_to_class(stripped)
    else:
        return " " * indent + f"# UNKNOWN: {stripped}"

def transpile(code: str) -> str:
    """transpile multiple lines of bracket codes"""
    lines = code.splitlines()
    result = []
    for line in lines:
        result.append(transpile_line(line))
    return "\n".join(result)
