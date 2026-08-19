#!/usr/bin/env python3
# bracket/CLASS.py
# manage classes defining

from keyword import kwlist

# [CLASS] [<class name>] [<parent class>] → class <class name>(<parent class>):
def CLASS_to_class(code: str):
    code = code.lstrip()
    keyword, rest = code.split(" ", 1)
    if keyword!="[CLASS]":
        raise SyntaxError(f"Expected `CLASS` got `{keyword}`.")
    inner = rest.removeprefix("[").removesuffix("]")
    parts = inner.split("] [")
    if len(parts) != 2:
        raise SyntaxError("Usage: [CLASS] [<class name>] [<parent class>]")
    class_name = parts[0].strip()
    parent_class = parts[1].strip()
    if not class_name:
        raise SyntaxError("Class name cannot be empty.")
    dangerous_list = kwlist+["INFO", "VAR", "INPUT", "IF", "ELSEIF", "ELSE", "FOR", "WHILE", "LOOP", "FUNC", "CLASS", "ERROR", "WARN", "USE"]
    if not class_name.isidentifier():
        raise SyntaxError(f"Invalid class name: {class_name}.")
    if class_name in dangerous_list:
        raise SyntaxError(f"Invalid name: {class_name}.")
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
