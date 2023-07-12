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


class Statement(pydantic.BaseModel):
    name: str
    args: list[Any]
