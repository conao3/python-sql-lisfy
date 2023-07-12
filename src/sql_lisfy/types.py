import pydantic


## Exceptions

class LisfyError(Exception):
    pass


class ReaderError(LisfyError):
    pass


class EvalError(LisfyError):
    pass


## Tokens

class Token(pydantic.BaseModel):
    name: str
