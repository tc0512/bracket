#!/usr/bin/env python3
# bracket/LOOP.py
# manage the loop sentences

# [FOR] [<range var>] [<start>, <end>, <step length>] → for <range var> in range(<start>, <end>, <step length>)
# BRANCH.py 或 LOOP.py
def FOR_to_for(code: str) -> str:
    code = code.lstrip()
    keyword, rest = code.split(" ", 1)
    if keyword != "[FOR]":
        raise SyntaxError(f"Expected `[FOR]` got `{keyword}`")
    var_part, range_part = rest.split(" ", 1)
    var = var_part.removeprefix("[").removesuffix("]")
    range_args = range_part.removeprefix("[").removesuffix("]")
    parts = [p.strip() for p in range_args.split(",")]
    if len(parts)!=3:
        raise SyntaxError("[FOR] needs 3 range arguments")
    start, end, step = parts
    return f"for {var} in range({start}, {end}, {step}):"
