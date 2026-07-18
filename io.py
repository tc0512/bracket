# bracket/io.py
# manage I/O operation

# [INFO] [<text>] → print(<text>)
def INFO_to_print(code: str):
    keyword, text = code.split(" ", 1)
    if keyword!="[INFO]":
        raise SyntaxError(f"Expected `[INFO]` got `{keyword}`")
    text = text.removeprefix("[").removesuffix("]")
    return f"print({text})"

# [INPUT] [<tip word>] [<multilines>] → input(<tip word>)
def INPUT_to_input(code: str):
    keyword = code.split(" ", 1)[0]
    if keyword != "[INPUT]":
        raise SyntaxError(f"Expected `[INPUT]` got `{keyword}`")
    rest = code.split(" ", 1)[1]
    inner = rest.removeprefix("[").removesuffix("]")
    parts = inner.split("][")
    if len(parts) != 2:
        raise SyntaxError("Usage: [INPUT] [<tip word>] [<multilines> (bool)]")
    tip_word = parts[0]
    multilines = parts[1].lower() == "true"
    if multilines:
        return f'''\
print("{tip_word} (use EOF to finish)")
lines = []
while True:
    try:
        line = input()
    except EOFError:
        break
    lines.append(line)
user_input = "\\n".join(lines)
'''
    else:
        return f'''\
user_input = input("{tip_word}: ")
'''
