from __future__ import annotations

from typing import Optional

import more_itertools

from . import types
from . import subr

def read(
    input_stream: more_itertools.peekable[str],
    eof_error_p: bool = True,
    eof_value: Optional[types.Token] = None,
    recursive_p: bool = False,
) -> types.Token:
    peek = subr.reader.peek_char(True, input_stream, False, 'EOF', recursive_p=recursive_p)

    if peek == 'EOF':
        if eof_error_p:
            raise types.ReaderError('unexpected EOF')

        if eof_value is None:
            raise types.ReaderError('eof_value must be provided if eof_error_p is False')

        return eof_value

    raise types.ReaderError(f'unexpected character: {peek}')
