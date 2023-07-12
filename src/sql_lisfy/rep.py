from typing import Optional

import more_itertools

from . import lexer
from . import types


def read(arg: str) -> Optional[str]:
    stream = more_itertools.peekable(arg)
    res = lexer.read(stream, eof_error_p=False, eof_value=types.Token(name='EOF'), recursive_p=False)
    if res.name == 'EOF':
        return None

    return str(res)


def eval(arg: Optional[str]) -> Optional[str]:
    return arg


def print(arg: Optional[str]) -> Optional[str]:
    return arg


def rep(arg: Optional[str]) -> Optional[str]:
    return print(eval(read(arg)))
