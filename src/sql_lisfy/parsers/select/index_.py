from __future__ import annotations
from typing import Any

import more_itertools

from ... import types
from ... import parser_subr

TOKENS = []

RESERVED_KEYWORDS = [
    'WITH',
    'SELECT',
    'FROM',
    'WHERE',
    'GROUP',
    'HAVING',
    'WINDOW',
    'UNION',
    'INTERSECT',
    'EXCEPT',
    'ORDER',
    'LIMIT',
    'OFFSET',
    'FETCH',
    'FOR',
]

def read_all_distinct(input_stream: more_itertools.peekable[types.Token], args: dict[str, Any]) -> None:
    if parser_subr.expect_token(input_stream, 'ALL'):
        args['all'] = True

    if parser_subr.expect_token(input_stream, 'DISTINCT'):
        args['distinct'] = True

        if parser_subr.expect_token(input_stream, 'ON'):
            exps = parser_subr.read_expr_list(input_stream)
            args['distinct_on'] = exps


def read_select_list(input_stream: more_itertools.peekable[types.Token], args: dict[str, Any]) -> None:
    res: list[types.Expression] = []
    while True:
        exp = parser_subr.read_expr(input_stream)

        if parser_subr.expect_token(input_stream, 'AS'):
            exp.args['alias'] = next(input_stream).name

        res.append(exp)

        if parser_subr.peek_expect_token(input_stream, RESERVED_KEYWORDS, allow_eof=True):
            break

        parser_subr.ensure_token(input_stream, ',')

    if res:
        args['select_list'] = res


def read_from_item(input_stream: more_itertools.peekable[types.Token]) -> types.Expression:
    return parser_subr.read_expr(input_stream)


def read_from(input_stream: more_itertools.peekable[types.Token], args: dict[str, Any]) -> None:
    breakpoint()
    if not parser_subr.expect_token(input_stream, 'FROM'):
        return

    res: list[types.Expression] = []
    while True:
        res.append(read_from_item(input_stream))

        if parser_subr.peek_expect_token(input_stream, RESERVED_KEYWORDS, allow_eof=True):
            break

        parser_subr.ensure_token(input_stream, ',')

    args['from'] = res


def read(input_stream: more_itertools.peekable[types.Token]) -> types.Statement:
    args = {}
    read_all_distinct(input_stream, args)
    read_select_list(input_stream, args)
    read_from(input_stream, args)

    return types.Statement(
        name='SELECT',
        args=args,
    )
