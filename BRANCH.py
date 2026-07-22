#!/usr/bin/env python3
# bracket/BRANCH.py
# manage the branch sentences

# [IF] [<cond>] → if cond:
def IF_to_if(code: str):
    code = code.lstrip()
    keyword, cond = code.split(" ", 1)
    if keyword!="[IF]":
        raise SyntaxError(f"Expect `[IF]` got {keyword}")
    text = cond.removeprefix("[").removesuffix("]")
    return f"if {text}:"
