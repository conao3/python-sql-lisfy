from __future__ import annotations

import more_itertools

from . import types
from . import parser_subr


def ensure_token(
    input_stream: more_itertools.peekable[types.Token],
    ensure: str,
):
    peek = input_stream.peek(None)
    if peek is None:
        raise types.ParserError('Unexpected EOF')

    if peek.name.upper() != ensure:
        raise types.ParserError(f'Expected `{ensure}` but got `{peek}`.')

    return next(input_stream)


def peek_expect_token(
    input_stream: more_itertools.peekable[types.Token],
    expect: str | list[str],
    allow_eof: bool = False,
):
    peek = input_stream.peek(None)
    if peek is None:
        return allow_eof

    if peek.name.upper() not in ([expect] if isinstance(expect, str) else expect):
        return False

    return True


def expect_token(
    input_stream: more_itertools.peekable[types.Token],
    expect: str | list[str],
    allow_eof: bool = False,
):
    if not peek_expect_token(input_stream, expect, allow_eof=allow_eof):
        return False

    _ = next(input_stream)
    return True


def expect_eof(input_stream: more_itertools.peekable[types.Token]) -> bool:
    peek = input_stream.peek(None)
    if peek is None:
        return True

    return False


def read_expr_positional_parameter(input_stream: more_itertools.peekable[types.Token]) -> types.Expression:
    _ = next(input_stream)  # consume $
    number = next(input_stream)
    return types.Expression(
        name='POSITIONAL PARAMETER',
        args={
            'number': number,
        },
    )


def read_expr_column_reference(input_stream: more_itertools.peekable[types.Token]) -> types.Expression:
    columnname = next(input_stream).name
    peek = input_stream.peek(None)
    if peek is None:
        return types.Expression(
            name='COLUMN REFERENCE',
            args={
                'columnname': columnname,
            },
        )

    if peek.name == '.':
        _ = next(input_stream)  # consume .
        correlation = columnname
        columnname = next(input_stream).name
        return types.Expression(
            name='COLUMN REFERENCE',
            args={
                'correlation': correlation,
                'columnname': columnname,
            },
        )

    return types.Expression(
        name='COLUMN REFERENCE',
        args={
            'columnname': columnname,
        }
    )


def read_expr(input_stream: more_itertools.peekable[types.Token]) -> types.Expression:
    peek = input_stream.peek(None)
    if peek is None:
        raise types.ParserError('Unexpected EOF')

    if peek.name == '$':
        return read_expr_positional_parameter(input_stream)

    return read_expr_column_reference(input_stream)


def read_expr_list(input_stream: more_itertools.peekable[types.Token]) -> list[types.Expression]:
    parser_subr.ensure_token(input_stream, '(')

    peek = input_stream.peek()
    if peek.name == ')':
        _ = next(input_stream)
        return []

    res: list[types.Expression] = []
    while True:
        res.append(read_expr(input_stream))

        if expect_token(input_stream, ')'):
            break

        ensure_token(input_stream, ',')

    return res
