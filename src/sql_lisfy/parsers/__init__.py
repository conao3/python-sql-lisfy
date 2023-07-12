from __future__ import annotations

import more_itertools

from .. import types

from . import select


def read(input_stream: more_itertools.peekable[types.Token]) -> types.Statement:
    peek = input_stream.peek(None)

    if peek is None:
        raise types.ParserError('Unexpected EOF')

    if peek.name.upper() == 'SELECT':
        _ = next(input_stream)
        return select.read(input_stream)

    raise types.ParserError(f'Unexpected token: {peek}')
