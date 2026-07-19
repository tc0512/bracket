#!/usr/bin/env python3
# bracket/IO.py
# manage I/O operation

# [INFO] [<text>] → print(<text>)
def INFO_to_print(code: str):
    keyword, text = code.split(" ", 1)
    if keyword!="[INFO]":
        raise SyntaxError(f"Expected `INFO` got `{keyword}`.")
    text = text.removeprefix("[").removesuffix("]")
    return f"print({text})"

# [VAR] [<var name>] [INPUT] [<tip word> (don't need quotation marks)] [<multilines> (bool)] → var = input(<tip word>)
def INPUT_to_input(code: str) -> str:
    rest = code.split(" ", 1)[1]
    inner = rest.removeprefix("[").removesuffix("]")
    parts = inner.split("] [")
    if len(parts) != 4:
        raise SyntaxError("Usage: [VAR] [<var name>] [INPUT] [<tip word> (don't need quotation marks)] [<multilines> (bool)]")
    var_name = parts[0].strip()
    keyword = parts[1]
    tip_word = parts[2].strip()
    multilines = parts[3].lower() in ("true", "1", "yes", "on")
    if not var_name:
        raise SyntaxError("Var name cannot be empty.")
    if not var_name.isidentifier():
        raise SyntaxError(f"Invalid var name: {var_name}.")
    if keyword != "INPUT":
        raise SyntaxError(f"Expected `INPUT`, got `{keyword}`.")
    if not tip_word:
        raise SyntaxError("Tip word cannot be empty")
    if multilines:
        return f'''\
print("{tip_word} (use EOF to finish)")
lines = []
while True:
    try:
        line = input()
    except EOFError:
        break
    except KeyboardInterrupt:
        print("\\\\nCanceled input.")
        break
    lines.append(line)
{var_name} = "\\\\n".join(lines)
'''
    else:
        return f'{var_name} = input("{tip_word}: ")'
