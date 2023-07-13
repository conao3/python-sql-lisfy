from typing import Any
import pydantic


## Exceptions

class LisfyError(Exception):
    pass


class LexerError(LisfyError):
    pass


class ParserError(LisfyError):
    pass


class EvalError(LisfyError):
    pass


## Tokens

class Token(pydantic.BaseModel):
    name: str


class Expression(pydantic.BaseModel):
    name: str
    args: dict[str, Any]


class Statement(pydantic.BaseModel):
    name: str
    args: dict[str, Any]
