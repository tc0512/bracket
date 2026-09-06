# bracket/IMPORTLIB.py
# manage libraries importing

# [USE] [<lib>] → import <lib>
def USE_to_import(code: str):
    code = code.lstrip()
    keyword, lib = code.split(" ", 1)
    if keyword!="[USE]":
        raise SyntaxError(f"Expect `[USE]` got {keyword}")
    key = lib.removeprefix("[").removesuffix("]")
    lib_dict = {
        "TKGUI": "tkinter as TKGUI",
        "PACKAGING": "PyInstaller.__main__\nPACK = PyInstaller.__main__.run"
    }
    return f"import {lib_dict[key]}"
