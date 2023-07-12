from __future__ import annotations
from typing import Callable, Optional

import more_itertools

from . import types
from . import subr


TERMINATING_MACRO_CHARS = ' "\'(),;'


def read_quote(input_stream: more_itertools.peekable[str]) -> types.Token:
    token = ''
    token += subr.reader.read_char(input_stream, recursive_p=True)  # read starting '

    while True:
        peek = subr.reader.peek_char(None, input_stream, recursive_p=True)
        if peek == "'":
            token += subr.reader.read_char(input_stream, recursive_p=True)  # read ending '
            break

        token += subr.reader.read_char(input_stream, recursive_p=True)

    return types.Token(name=token)


def read_double_quote(input_stream: more_itertools.peekable[str]) -> types.Token:
    token = ''
    token += subr.reader.read_char(input_stream, recursive_p=True)  # read starting '

    while True:
        peek = subr.reader.peek_char(None, input_stream, recursive_p=True)
        if peek == '"':
            token += subr.reader.read_char(input_stream, recursive_p=True)  # read ending '
            break

        token += subr.reader.read_char(input_stream, recursive_p=True)

    return types.Token(name=token)


def read_single_token(input_stream: more_itertools.peekable[str]) -> types.Token:
    token = subr.reader.read_char(input_stream, recursive_p=True)
    return types.Token(name=token)


def read_token(input_stream: more_itertools.peekable[str]) -> types.Token:
    token = ''
    while True:
        peek = subr.reader.peek_char(None, input_stream, eof_error_p=False, eof_value=' ', recursive_p=True)
        if peek in TERMINATING_MACRO_CHARS:
            break

        token += subr.reader.read_char(input_stream, recursive_p=True)

    return types.Token(name=token)


macro_handler: dict[str, Callable[[more_itertools.peekable[str]], types.Token]] = {
    '"': read_double_quote,
    "'": read_quote,
    '(': read_single_token,
    ')': read_single_token,
    ',': read_single_token,
    ';': read_single_token,
}

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

        handler = macro_handler.get(peek, read_token)
        res.append(handler(input_stream))

    return res
