#!/usr/bin/env python3
# bracket/VAR.py
# manage variables

from keyword import kwlist
import sys

import rich

# [VAR] [<var name>] [<value>] → <var name> = <value>
def VAR_to_varname_equal(code: str):
    code = code.lstrip()
    keyword, rest = code.split(" ", 1)
    if keyword!="[VAR]":
        rich.print(f"[red]{code}[/red]")
        rich.print(f"[red]error:Expected `VAR` got `{keyword}`.[/red]")
        sys.exit(1)
    inner = rest.removeprefix("[").removesuffix("]")
    parts = inner.split("] [")
    if len(parts) != 2:
        rich.print(f"[red]{code}[/red]")
        rich.print("[red]error:Something wrong in your code[/red]")
        rich.print("[red]the true usage of `[VAR]` sentences is `[VAR] [<var name>] [<value>]`[red]")
        sys.exit(1)
    var_name = parts[0].strip()
    value = parts[1].strip()
    if not var_name:
        rich.print(f"[red]{code}[/red]")
        rich.print("[red]error:Var name cannot be empty.[/red]")
        sys.exit(1)
    dangerous_list = kwlist+["INFO", "VAR", "INPUT", "IF", "ELSEIF", "ELSE", "FOR", "WHILE", "LOOP", "FUNC", "CLASS", "ERROR", "WARN", "USE"]
    if not var_name.isidentifier():
        rich.print(f"[red]{code}[/red]")
        rich.print(f"[red]error:Invalid var name: {var_name}.[/red]")
        sys.exit(1)
    if var_name in dangerous_list:
        rich.print(f"[red]{code}[/red]")
        rich.print(f"[red]error:Invalid var name: {var_name}.[/red]")
        sys.exit(1)
    if not value:
        rich.print(f"[red]{code}[/red]")
        rich.print("[red]error:Value cannot be empty.[/red]")
        sys.exit(1)
    return f"{var_name} = {value}"

def transpile_line(line: str):
    """transpile one line of bracket code and operate indents"""
    indent = len(line) - len(line.lstrip())
    stripped = line.lstrip()
    if not stripped:
        return ""
    if stripped.startswith("[VAR]"):
        return " " * indent + VAR_to_varname_equal(stripped)
    else:
        return " " * indent + f"# UNKNOWN: {stripped}"

def transpile(code: str) -> str:
    """transpile multiple lines of bracket codes"""
    lines = code.splitlines()
    result = []
    for line in lines:
        result.append(transpile_line(line))
    return "\n".join(result)
