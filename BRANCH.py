#!/usr/bin/env python3
# bracket/BRANCH.py
# manage the branch sentences

# [IF] [<cond>] → if <cond>:
def IF_to_if(code: str):
    code = code.lstrip()
    keyword, cond = code.split(" ", 1)
    if keyword!="[IF]":
        raise SyntaxError(f"Expect `[IF]` got {keyword}")
    text = cond.removeprefix("[").removesuffix("]")
    return f"if {text}:"

# [ELSEIF] [<cond>] → elif <cond>:
def ELSEIF_to_elif(code: str):
    code = code.lstrip()
    keyword, cond = code.split(" ", 1)
    if keyword!="[ELSEIF]":
        raise SyntaxError(f"Expect `[ELSEIF]` got {keyword}")
    text = cond.removeprefix("[").removesuffix("]")
    return f"elif {text}:"

# [ELSE] → else:
def ELSE_to_else(code: str):
    code = code.lstrip()
    if code!="[ELSE]":
        raise SyntaxError(f"Expect `[ELSE]` got {code}")
    return "else":

def transpile_line(line: str):
    indent = len(line) - len(line.lstrip())
    stripped = line.lstrip()
    if not stripped:
        return ""
    if stripped.startswith("[IF]"):
        return " " * indent + IF_to_if(stripped)
    elif stripped.startswith("[ELSEIF]"):
        return " " * indent + ELSEIF_to_elif(stripped)
    elif stripped == "[ELSE]":
        return " " * indent + ELSE_to_else(stripped)
    else:
        return " " * indent + f"# UNKNOWN: {stripped}"

def transpile(code: str):
    lines = code.splitlines()
    result = []
    for line in lines:
        result.append(transpile_line(line))
    return "\n".join(result)
