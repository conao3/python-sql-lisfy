from typing import Optional


def read(arg: Optional[str]) -> Optional[str]:
    return arg


def eval(arg: Optional[str]) -> Optional[str]:
    return arg


def print(arg: Optional[str]) -> Optional[str]:
    return arg


def rep(arg: Optional[str]) -> Optional[str]:
    return print(eval(read(arg)))
