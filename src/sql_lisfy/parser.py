from __future__ import annotations

from typing import Optional

import more_itertools

from . import types
from . import parsers


def read(
    input_stream: more_itertools.peekable[types.Token],
    eof_error_p: bool = True,
    eof_value: Optional[types.Statement] = None,
    recursive_p: bool = False,
) -> types.Statement:
    peek = input_stream.peek(None)

    if peek is None:
        if eof_error_p:
            raise types.ParserError('Unexpected EOF')

        if eof_value is None:
            raise ValueError('eof_value must be specified if eof_error_p is False')

        return eof_value

    return parsers.read(input_stream)
