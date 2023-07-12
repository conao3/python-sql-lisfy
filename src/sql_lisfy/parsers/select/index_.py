from __future__ import annotations

import more_itertools

from .. import types

TOKENS = []


def read(input_stream: more_itertools.peekable[types.Token]) -> types.Statement:
    return types.Statement(
        name='SELECT',
        args=[],
    )
