from __future__ import annotations
from typing import Any

import more_itertools

from ... import types
from ... import parser_subr

TOKENS = []


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

        if (
            parser_subr.expect_token(input_stream, 'FROM') or
            parser_subr.expect_token(input_stream, 'WHERE') or
            parser_subr.expect_token(input_stream, 'GROUP') or
            parser_subr.expect_token(input_stream, 'HAVING') or
            parser_subr.expect_token(input_stream, 'WINDOW') or
            parser_subr.expect_token(input_stream, 'UNION') or
            parser_subr.expect_token(input_stream, 'INTERSECT') or
            parser_subr.expect_token(input_stream, 'EXCEPT') or
            parser_subr.expect_token(input_stream, 'ORDER') or
            parser_subr.expect_token(input_stream, 'LIMIT') or
            parser_subr.expect_token(input_stream, 'OFFSET') or
            parser_subr.expect_token(input_stream, 'FETCH') or
            parser_subr.expect_token(input_stream, 'FOR') or
            parser_subr.expect_eof(input_stream)
        ):
            break

        parser_subr.ensure_token(input_stream, ',')

    if res:
        args['select_list'] = res


def read(input_stream: more_itertools.peekable[types.Token]) -> types.Statement:
    args = {}
    read_all_distinct(input_stream, args)
    read_select_list(input_stream, args)

    return types.Statement(
        name='SELECT',
        args=args,
    )
