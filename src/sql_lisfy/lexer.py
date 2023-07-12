from __future__ import annotations

import more_itertools

from . import types
from . import subr

def read(
    input_stream: more_itertools.peekable[str],
    eof_error_p: bool = True,
    eof_value: list[types.Token] = [],
    recursive_p: bool = False,
) -> list[types.Token]:
    peek = subr.reader.peek_char(True, input_stream, False, 'EOF', recursive_p=recursive_p)

    if peek == 'EOF':
        if eof_error_p:
            raise types.ReaderError('unexpected EOF')

        return eof_value

    raise types.ReaderError(f'unexpected character: {peek}')
