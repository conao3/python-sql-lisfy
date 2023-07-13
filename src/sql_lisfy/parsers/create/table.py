from __future__ import annotations

import more_itertools

from ... import types

TOKENS = ['TABLE']


def read(input_stream: more_itertools.peekable[types.Token]) -> types.Statement:
    args = {}

    return types.Statement(
        name='CREATE TABLE',
        args=args,
    )
