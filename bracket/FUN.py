#!/usr/bin/env python3
# bracket/FUN.py
# mamage function defining

from keyword import kwlist

# [FUNC] [<function name>] [<args>] → def <function name>(<args>):
def FUNC_to_def(code: str):
    code = code.lstrip()
    keyword, rest = code.split(" ", 1)
    if keyword!="[FUNC]":
        raise SyntaxError(f"Expected `FUNC` got `{keyword}`.")
    inner = rest.removeprefix("[").removesuffix("]")
    parts = inner.split("] [")
    if len(parts) != 2:
        raise SyntaxError("Usage: [FUNC] [<function name>] [<args>]")
    function_name = parts[0].strip()
    args = parts[1].strip()
    if not function_name:
        raise SyntaxError("Function name cannot be empty.")
    dangerous_list = kwlist+["INFO", "VAR", "INPUT", "IF", "ELSEIF", "ELSE", "FOR", "WHILE", "LOOP", "FUNC", "CLASS", "ERROR", "WARN", "USE"]
    if not function_name.isidentifier():
        raise SyntaxError(f"Invalid function name: {function_name}.")
    if function_name in dangerous_list:
        raise SyntaxError(f"Invalid function name: {function_name}.")
    if not args:
        raise SyntaxError("Value cannot be empty.")
    return f"def {function_name}({args}):"

# [RETURN] [<val>] → return <val>
def RETURN_to_return(code: str):
    code = code.lstrip()
    keyword, val = code.split(" ", 1)
    if keyword!="[RETURN]":
        raise SyntaxError(f"Expected `RETURN` got `{keyword}`.")
    val = val.removeprefix("[").removesuffix("]")
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
