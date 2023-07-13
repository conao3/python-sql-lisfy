from __future__ import annotations
from typing import Any

import more_itertools

from ... import types
from ... import parser_subr

TOKENS = []


def read_all_distinct(input_stream: more_itertools.peekable[types.Token], arg: dict[str, Any]) -> None:
    peek = input_stream.peek(None)
    if peek is None:
        return

    if peek.name.upper() == 'ALL':
        _ = next(input_stream)  # consume ALL
        arg['all'] = True

    elif peek.name.upper() == 'DISTINCT':
        _ = next(input_stream)  # consume DISTINCT
        arg['distinct'] = True

        peek = input_stream.peek(None)
        if peek is None:
            return

        if peek.name.upper() == 'ON':
            _ = next(input_stream)  # consume ON
            exps = parser_subr.read_expr_list(input_stream)
            arg['distinct_on'] = exps


def read(input_stream: more_itertools.peekable[types.Token]) -> types.Statement:
    args = {}
    read_all_distinct(input_stream, args)

    return types.Statement(
        name='SELECT',
        args=args,
    )
