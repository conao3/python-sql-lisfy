from typing import Optional

import more_itertools

from . import lexer
from . import parser
from . import types


def read(arg: str) -> Optional[str]:
    stream = more_itertools.peekable(arg)
    res = lexer.read(stream, eof_error_p=False, eof_value=[], recursive_p=False)
    if res == []:
        return None

    token_stream = more_itertools.peekable(res)
    eof_statement = types.Statement(name='EOF', args=[])
    parser_res = parser.read(token_stream, eof_error_p=False, eof_value=eof_statement, recursive_p=False)
    if parser_res == eof_statement:
        return None

    return str(parser_res)


def eval(arg: Optional[str]) -> Optional[str]:
    if arg:
        return arg


def print(arg: Optional[str]) -> Optional[str]:
    if arg:
        return arg


def rep(arg: str) -> Optional[str]:
    return print(eval(read(arg)))
