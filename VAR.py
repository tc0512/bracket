#!/usr/bin/env python3
# bracket/VAR.py
# manage variables

# [VAR] [<var name>] [<value>] → <var name> = <value>
def VAR_to_varname_equal(code: str):
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
