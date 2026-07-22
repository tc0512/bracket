#!/usr/bin/env python3
# bracket/VAR.py
# manage variables

# [VAR] [<var name>] [<value>] → <var name> = <value>
def VAR_to_varname_equal(code: str):
    code = code.lstrip()
    keyword, rest = code.split(" ", 1)
    if keyword!="[VAR]":
        raise SyntaxError(f"Expected `VAR` got `{keyword}`.")
    inner = rest.removeprefix("[").removesuffix("]")
    parts = inner.split("] [")
    if len(parts) != 2:
        raise SyntaxError("Usage: [VAR] [<var name>] [<value>]")
    var_name = parts[0].strip()
    value = parts[1].strip()
    if not var_name:
        raise SyntaxError("Var name cannot be empty.")
    if not var_name.isidentifier():
        raise SyntaxError(f"Invalid var name: {var_name}.")
    if not value:
        raise SyntaxError("Value cannot be empty.")
    return f"{var_name} = {value}"

def transpile_line(line: str) -> str:
    """转译一行 bracket 代码，自动处理缩进"""
    indent = len(line) - len(line.lstrip())
    stripped = line.lstrip()

    if not stripped:
        return ""

    if stripped.startswith("[VAR]"):
        return " " * indent + VAR_to_varname_equal(stripped)
    else:
        return " " * indent + f"# UNKNOWN: {stripped}"

def transpile(code: str) -> str:
    """转译多行 bracket 代码"""
    lines = code.splitlines()
    result = []
    for line in lines:
        result.append(transpile_line(line))
    return "\n".join(result)
