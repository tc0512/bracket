#!/usr/bin/env python3
# bracket/WARN.py
# manage warnings generating

# [WARN] [<info>] → __import__("rich").print("[yellow]<info>[/yellow]")
def WARN_to_rich_print(code: str):
    code = code.lstrip()
    keyword, info = code.split(" ", 1)
    if keyword!="[WARN]":
        raise SyntaxError(f"Expected `WARN` got `{keyword}`.")
    info = info.removeprefix("[").removesuffix("]")
    return f"__import__('rich').print('[yellow]{info[1:-1]}[/yellow]')"

def transpile_line(line: str) -> str:
    """transpile one line of bracket code and operate indents"""
    indent = len(line) - len(line.lstrip())
    stripped = line.lstrip()
    if not stripped:
        return ""
    if stripped.startswith("[WARN]"):
        return " " * indent + WARN_to_rich_print(stripped)
    else:
        return " " * indent + f"# UNKNOWN: {stripped}"

def transpile(code: str) -> str:
    """transpile multiple lines of bracket codes"""
    lines = code.splitlines()
    result = []
    for line in lines:
        result.append(transpile_line(line))
    return "\n".join(result)
