from __future__ import annotations
from typing import Optional

import more_itertools

from . import types
from . import subr


def read_token(
    input_stream: more_itertools.peekable[str],
    eof_error_p: bool = True,
    eof_value: types.Token = types.Token(name='EOF'),
    recursive_p: bool = False,
) -> types.Token:
    token = ''
    while True:
        peek = subr.reader.peek_char(None, input_stream, eof_error_p=False, eof_value=' ', recursive_p=True)
        if peek.isspace():
            break

        token += subr.reader.read_char(input_stream, recursive_p=True)

    return types.Token(name=token)


def read(
    input_stream: more_itertools.peekable[str],
    eof_error_p: bool = True,
    eof_value: Optional[list[types.Token]] = None,
    recursive_p: bool = False,
) -> list[types.Token]:
    res: list[types.Token] = []

    while True:
        peek = subr.reader.peek_char(True, input_stream, False, 'EOF', recursive_p=recursive_p)

        if peek == 'EOF':
            break

        res.append(read_token(input_stream, recursive_p=True))

    return res
