# bracket/io.py
# manage I/O operation

# [INFO] [<text>] → print(<text>)
def INFO_to_print(code: str):
    keyword, text = code.split(" ", 1)
    if keyword!="[INFO]":
        raise SyntaxError(f"Expected `[INFO]` got `{keyword}`")
    text = text.removeprefix("[").removesuffix("]")
    return f"print({text})"
