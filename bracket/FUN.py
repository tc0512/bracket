#!/usr/bin/env python3
# bracket/FUN.py
# mamage function defining

from keyword import kwlist
import sys

import rich

# [FUNC] [<function name>] [<args>] → def <function name>(<args>):
def FUNC_to_def(code: str):
    code = code.lstrip()
    keyword, rest = code.split(" ", 1)
    if keyword!="[FUNC]":
        rich.print(f"[red]{code}[/red]")
        rich.print(f"[red]error:Expected `FUNC` got `{keyword}`.[/red]")
        sys.exit(1)
    inner = rest.removeprefix("[").removesuffix("]")
    parts = inner.split("] [")
    if len(parts) != 2:
        rich.print(f"[red]{code}[red]")
        rich.print("[red]error:Something wrong in your code[/red]")
        rich.print("[red]The usage of `[FUNC]` sentences is `[FUNC] [<function name>] [<args>]`[/red]")
        sys.exit(1)
    function_name = parts[0].strip()
    args = parts[1].strip()
    if not function_name:
        rich.print(f"[red]{code}[/red]")
        rich.print("[/red]error:Function name cannot be empty.[/red]")
        sys.exit(1)
    dangerous_list = kwlist+["INFO", "VAR", "INPUT", "IF", "ELSEIF", "ELSE", "FOR", "WHILE", "LOOP", "FUNC", "CLASS", "ERROR", "WARN", "USE"]
    if not function_name.isidentifier():
        rich.print(f"[red]{code}[/red]")
        rich.print(f"[red]error:Invalid function name: {function_name}.[/red]")
        sys.exit(1)
    if function_name in dangerous_list:
        rich.print(f"[red]{code}[/red]")
        rich.print(f"[red]error:Invalid function name: {function_name}.[/red]")
        sys.exit(1)
    return f"def {function_name}({args}):"

# [RETURN] [<val>] → return <val>
def RETURN_to_return(code: str):
    code = code.lstrip()
    keyword, val = code.split(" ", 1)
    if keyword!="[RETURN]":
        rich.print(f"[red]{code}[/red]")
        rich.print(f"[red]error:Expected `FUNC` got `{keyword}`.[/red]")
        sys.exit(1)
    val = val.removeprefix("[").removesuffix("]")
    if not val:
        return "return"
    return f"return {val}"

def transpile_line(line: str) -> str:
    """transpile one line of bracket code and operate indents"""
    indent = len(line) - len(line.lstrip())
    stripped = line.lstrip()
    if not stripped:
        return ""
    if stripped.startswith("[FUNC]"):
        return " " * indent + FUNC_to_def(stripped)
    if stripped.startswith("[RETURN]"):
        return " " * indent + RETURN_to_return(stripped)
    else:
        return " " * indent + f"# UNKNOWN: {stripped}"

def transpile(code: str) -> str:
    """transpile multiple lines of bracket codes"""
    lines = code.splitlines()
    result = []
    for line in lines:
        result.append(transpile_line(line))
    return "\n".join(result)
