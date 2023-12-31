from __future__ import annotations

import more_itertools

from ... import types

from ... import parser_subr
from . import table

TOKENS = ['CREATE']


def read(input_stream: more_itertools.peekable[types.Token]) -> types.Statement:
    peek = input_stream.peek(None)

    if peek is None:
        raise types.ParserError('Unexpected EOF')

    if parser_subr.expect_token(input_stream, 'TABLE'):
        return table.read(input_stream)

    raise types.ParserError(f'Unexpected token: {peek}')
