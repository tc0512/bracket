#!/usr/bin/env python3
# bracket/IO.py
# manage I/O operation

from keyword import kwlist
import sys

import rich
# [INFO] [<text>] → print(<text>)
def INFO_to_print(code: str):
    code = code.lstrip()
    keyword, text = code.split(" ", 1)
    if keyword!="[INFO]":
        rich.print(f"[red]{code}[/red]")
        rich.print(f"[red]error:Expected `INFO` got `{keyword}`.[/red]")
        sys.exit(1)
    text = text.removeprefix("[").removesuffix("]")
    return f"print({text})"

# [VAR] [<var name>] [INPUT] [<tip word>] [<multilines> (bool)] → var = input(<tip word>)
def INPUT_to_input(code: str):
    code = code.lstrip()
    rest = code.split(" ", 1)[1]
    inner = rest.removeprefix("[").removesuffix("]")
    parts = inner.split("] [")
    if len(parts) != 4:
        rich.print(f"[red]{code}[/red]")
        rich.print("[red]error:Something wrong in your code.[/red]")
        rich.print("[red]The true usage of `[INPUT]` sentences is `[VAR] [<var name>] [INPUT] [<tip word>] [<multilines> (bool)]`[/red]")
        sys.exit(1)
    var_name = parts[0].strip()
    keyword = parts[1]
    tip_word = parts[2].strip()
    multilines = parts[3].lower() in ("true", "1", "yes", "on")
    if not var_name:
        rich.print(f"[red]{code}[/red]")
        rich.print("[red]error:Var name cannot be empty.[/red]")
        sys.exit(1)
    if not var_name.isidentifier():
        rich.print(f"[red]{code}[/red]")
        rich.print(f"[red]error:Invalid var name: {var_name}.[/red]")
        sys.exit(1)
    dangerous_list = kwlist+["INFO", "VAR", "INPUT", "IF", "ELSEIF", "ELSE", "FOR", "WHILE", "LOOP", "FUNC", "CLASS", "ERROR", "WARN", "USE"]
    if var_name in dangerous_list:
        rich.print(f"[red]{code}[/red]")
        rich.print(f"[red]error:Invalid var name: {var_name}.[/red]")
        sys.exit(1)
    if keyword != "INPUT":
        rich.print(f"[red]{code}[/red]")
        rich.print(f"[red]error:Expected `INPUT` got `{keyword}`.[/red]")
        sys.exit(1)
    if multilines:
        return f'''\
print({tip_word})
lines = []
while True:
    try:
        line = input()
    except EOFError:
        break
    except KeyboardInterrupt:
        print("\\nCanceled input.")
        break
    lines.append(line)
{var_name} = "\\n".join(lines)
'''
    else:
        return f'{var_name} = input({tip_word})'

def transpile_line(line: str):
    """transpile one line of bracket code and operate indents"""
    indent = len(line) - len(line.lstrip())
    stripped = line.lstrip()

    if stripped.startswith("[INFO]"):
        return " " * indent + INFO_to_print(stripped)
    elif "[INPUT]" in stripped:
        return " " * indent + INPUT_to_input(stripped)
    elif stripped.startswith("[VAR]"):
        return " " * indent + VAR_to_varname_equal(stripped)
    else:
        return " " * indent + f"# UNKNOWN: {stripped}"


def transpile(code: str) -> str:
    """Transpile multiple lines of bracket code"""
    lines = code.splitlines()
    result = []
    for line in lines:
        if line.strip() == "":
            result.append("")
        else:
            result.append(transpile_line(line))
    return "\n".join(result)
