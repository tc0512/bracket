#!/usr/bin/env python3
# bracket/transpile.py
# Unification transpile interface

from .IO import INFO_to_print, INPUT_to_input
from .VAR import VAR_to_varname_equal
from .BRANCH import IF_to_if, ELSEIF_to_elif, ELSE_to_else
from .LOOP import (
    FOR_to_for,
    WHILE_to_while,
    LOOP_to_while_True,
    BREAK_to_break,
    CONTINUE_to_continue,
)
from .IMPORTLIB import USE_to_import


def transpile_line(line: str) -> str:
    indent = len(line) - len(line.lstrip())
    stripped = line.lstrip().split("#")[0].rstrip()
    if not stripped:
        return ""
    for i in ["print", "import", "def", "class", "exec", "__import__"]:
        if i in stripped:
            raise SyntaxError("Sorry, we don't support python syntax.")
    if stripped.startswith("[USE]"):
        return " " * indent + USE_to_import(stripped)
    elif stripped.startswith("[FOR]"):
        return " " * indent + FOR_to_for(stripped)
    elif stripped.startswith("[WHILE]"):
        return " " * indent + WHILE_to_while(stripped)
    elif stripped == "[LOOP]":
        return " " * indent + LOOP_to_while_True(stripped)
    elif stripped == "[BREAK]":
        return " " * indent + BREAK_to_break(stripped)
    elif stripped == "[CONTINUE]":
        return " " * indent + CONTINUE_to_continue(stripped)
    elif stripped.startswith("[IF]"):
        return " " * indent + IF_to_if(stripped)
    elif stripped.startswith("[ELSEIF]"):
        return " " * indent + ELSEIF_to_elif(stripped)
    elif stripped == "[ELSE]":
        return " " * indent + ELSE_to_else(stripped)
    elif "[INPUT]" in stripped:
        return " " * indent + INPUT_to_input(stripped)
    elif stripped.startswith("[VAR]"):
        return " " * indent + VAR_to_varname_equal(stripped)
    elif stripped.startswith("[INFO]"):
        return " " * indent + INFO_to_print(stripped)
    return " " * indent + line

def transpile(code: str) -> str:
    lines = code.splitlines()
    result = []
    for line in lines:
        if line.strip():
            result.append(transpile_line(line))
        else:
            result.append("")
    return "\n".join(result)

# Tests
code = """
# 测试代码

# 1 打印
[INFO] ["Hello world!"]

# 2 变量
[VAR] [a] [3] #int
[VAR] [b] [2.0] #float
[VAR] [string] ["abc"] #string
[VAR] [lst] [[1, 2, 3, 4, 5]] #list
[VAR] [t] [(1, 2, 3)] #tuple
[VAR] [dict] [{1: 1, 2: 4, 3: 9}] #dictonary
[VAR] [bl] [True] #bool

# 3 输入
[VAR] [stdin] [INPUT] ['单行输入'] [False]
[VAR] [long] [INPUT] ['多行输入'] [True]

# 4 分支语句
[IF] [a>b]
    [INFO] ["大于"]

# 5 循环
[VAR] [total] [0]
[FOR] [i] [1, 101, 1]
    total+=i
[INFO] [f'1-100的和{total}']
"""
print(transpile(code))
