#!/usr/bin/env python3
# bracket/LOOP.py
# manage the loop sentences

import sys

import rich

# [FOR] [<range var>] [<start>, <end>, <step length>] → for <range var> in range(<start>, <end>, <step length>)
def FOR_to_for(code: str) -> str:
    code = code.lstrip()
    keyword, rest = code.split(" ", 1)
    if keyword != "[FOR]":
        rich.print(f"[red]{code}[/red]")
        rich.print(f"[red]error:Expected `[FOR]` got `{keyword}`[/red]")
        sys.exit(1)
    var_part, range_part = rest.split(" ", 1)
    var = var_part.removeprefix("[").removesuffix("]")
    range_args = range_part.removeprefix("[").removesuffix("]")
    parts = [p.strip() for p in range_args.split(",")]
    if len(parts)!=3:
        rich.print(f"[red]{code}[/red]")
        rich.print("[red]error:[FOR] needs 3 range arguments[/red]")
        sys.exit(1)
    start, end, step = parts
    return f"for {var} in range({start}, {end}, {step}):"

# [WHILE] [<cond>] → while <cond>:
def WHILE_to_while(code: str):
    code = code.lstrip()
    keyword, cond = code.split(" ", 1)
    if keyword!="[WHILE]":
        rich.print(f"[red]{code}[/red]")
        rich.print(f"[red]error:Expected `[WHILE]` got `{keyword}`[/red]")
        sys.exit(1)
    text = cond.removeprefix("[").removesuffix("]")
    return f"while {text}:"

# [LOOP] → while True:
def LOOP_to_while_True(code: str):
    code = code.lstrip()
    if code!="[LOOP]":
        rich.print(f"[red]{code}[/red]")
        rich.print(f"[red]error:Expected `[LOOP]` got `{keyword}`[/red]")
        sys.exit(1)
    return "while True:"

# [CONTINUE] → continue
def CONTINUE_to_continue(code: str):
    code = code.lstrip()
    if code!="[CONTINUE]":
        rich.print(f"[red]{code}[/red]")
        rich.print(f"[red]error:Expected `[CONTINUE]` got `{keyword}`[/red]")
        sys.exit(1)
    return "continue"

# [BREAK] → break
def BREAK_to_break(code: str):
    code = code.lstrip()
    if code!="[BREAK]":
        rich.print(f"[red]{code}[/red]")
        rich.print(f"[red]error:Expected `[BREAK]` got `{keyword}`[/red]")
        sys.exit(1)
    return "break"

def transpile_line(line: str) -> str:
    indent = len(line) - len(line.lstrip())
    stripped = line.lstrip()
    if not stripped:
        return ""
    if stripped.startswith("[FOR]"):
        return " " * indent + FOR_to_for(stripped)
    elif stripped.startswith("[WHILE]"):
        return " " * indent + WHILE_to_while(stripped)
    elif stripped == "[LOOP]":
        return " " * indent + LOOP_to_while_True(stripped)
    elif stripped == "[BREAK]":
        return " " * indent + BREAK_to_break(stripped)
    elif stripped == "[CONTINUE]":
        return " " * indent + CONTINUE_to_continue(stripped)
    else:
        return " " * indent + f"# UNKNOWN: {stripped}"

def transpile(code: str):
    lines = code.splitlines()
    result = []
    for line in lines:
        if line.strip():
            result.append(transpile_line(line))
        else:
            result.append("")
    return "\n".join(result)
