#!/usr/bin/python3
# bracket/BRANCH.py
# manage branch sentences

import re

from .IO import INFO_to_print, INPUT_to_input
from .VAR import VAR_to_varname_equal

def indent(code: str, spaces: int = 4) -> str:
    """Tab the codes."""
    return "\n".join(" " * spaces + line for line in code.split("\n"))

def parse_condition(line: str) -> str:
    """Extract conditions from [IF] [cond] or [ELSEIF] [cond]"""
    line = line.lstrip()
    parts = line.split(" ", 1)
    if len(parts) < 2:
        raise SyntaxError(f"Missing condition: {line}")
    rest = parts[1]
    match = re.search(r'\[([^\]]*)\]', rest)
    if match:
        return match.group(1)
    raise SyntaxError(f"Cannot parse condition: {line}")

def parse_block(lines: list[str], start: int) -> tuple[list[str], int]:
    """Analysis the {} blocks,return the list of the contents of the blocks and the  finish position."""
    block = []
    i = start
    while i < len(lines):
        line = lines[i].strip()
        if line == "}":
            return block, i
        block.append(line)
        i += 1
    raise SyntaxError(f"Unmatched `{{` at line {start}")

def transpile_leaf(line: str) -> str:
    """transpile one line of command which isn't a branch sentence."""
    line = line.strip()
    if line.startswith("[INFO]"):
        return INFO_to_print(line)
    elif line.startswith("[INPUT]"):
        return INPUT_to_input(line)
    elif line.startswith("[VAR]"):
        return VAR_to_varname_equal(line)
    else:
        return f"# UNKNOWN: {line}"

def IF_to_if(line: str, lines: list[str], i: int) -> tuple[str, int]:
    """
    Analysis the [IF] blocks,including [ELSEIF] and [ELSE]
    return the generated Python code string and the finish position
    """
    cond = parse_condition(line)
    body, i = parse_block(lines, i + 1)
    body_code = "\n".join(transpile_leaf(l) for l in body)
    result_parts = [f"if {cond}:"]
    result_parts.append(indent(body_code))
    while i < len(lines):
        next_line = lines[i].strip()
        if next_line.startswith("[ELSEIF]"):
            cond = parse_condition(next_line)
            body, i = parse_block(lines, i + 1)
            body_code = "\n".join(transpile_leaf(l) for l in body)
            result_parts.append(f"elif {cond}:")
            result_parts.append(indent(body_code))
        elif next_line == "[ELSE]":
            body, i = parse_block(lines, i + 1)
            body_code = "\n".join(transpile_leaf(l) for l in body)
            result_parts.append("else:")
            result_parts.append(indent(body_code))
            break
        else:
            break
    return "\n".join(result_parts), i
