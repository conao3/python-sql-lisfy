from typing import Optional

import more_itertools

from . import lexer


def read(arg: str) -> Optional[str]:
    stream = more_itertools.peekable(arg)
    res = lexer.read(stream, eof_error_p=False, eof_value=[], recursive_p=False)
    if res == []:
        return None

    return str(res)


def eval(arg: Optional[str]) -> Optional[str]:
    if arg:
        return arg


def print(arg: Optional[str]) -> Optional[str]:
    if arg:
        return arg


def rep(arg: str) -> Optional[str]:
    return print(eval(read(arg)))
