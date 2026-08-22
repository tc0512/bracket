#!/usr/bin/env python3
# bracket/ERROR.py
# manage errors generating

# [ERROR] [<info>] → __import__("rich").print([red]<info>[/red]);__import__("sys").exit(1)
def ERROR_to_rich_print_and_exit_1(code: str):
    code = code.lstrip()
    keyword, info = code.split(" ", 1)
    if keyword!="[ERROR]":
        raise SyntaxError(f"Expected `ERROR` got `{keyword}`.")
    info = info.removeprefix("[").removesuffix("]")
    return f"__import__('rich').print('[red]{info[1:-1]}[/red]');__import__('sys').exit(1)"

def transpile_line(line: str) -> str:
    """transpile one line of bracket code and operate indents"""
    indent = len(line) - len(line.lstrip())
    stripped = line.lstrip()
    if not stripped:
        return ""
    if stripped.startswith("[ERROR]"):
        return " " * indent + ERROR_to_rich_print_and_exit_1(stripped)
    else:
        return " " * indent + f"# UNKNOWN: {stripped}"

def transpile(code: str) -> str:
    """transpile multiple lines of bracket codes"""
    lines = code.splitlines()
    result = []
    for line in lines:
        result.append(transpile_line(line))
    return "\n".join(result)
