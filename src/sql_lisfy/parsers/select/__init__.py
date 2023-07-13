from __future__ import annotations

import more_itertools

from .. import types

from . import index_

TOKENS = ['SELECT']


def read(input_stream: more_itertools.peekable[types.Token]) -> types.Statement:
    peek = input_stream.peek(None)

    if peek is None:
        raise types.ParserError('Unexpected EOF')

    return index_.read(input_stream)
