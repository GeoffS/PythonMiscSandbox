import types
from typing import Protocol


class Thingy():
    pass


def thingy_method(self) -> str:
    return f"thingy_method: {self}"


class A(Protocol):
    one: int
    two: int
    def name(self) -> str: ...


class B(Protocol):
    three: int
    four: int
    def name(self) -> str: ...


if __name__ == '__main__':
    a: A = Thingy()
    a.one = 1
    a.two = 2
    a_thingy_method = types.MethodType(thingy_method, a)
    print(f"a_thingy_method = {a_thingy_method}")
    print(f"a_thingy_method() = {a_thingy_method()}")
    a.name = a_thingy_method

    b: B = Thingy()
    b.three = 3
    b.four = 4
    b_lambda = types.MethodType(lambda self: f"b_lambda: {self}", b)
    b.name = b_lambda

    print(f"a.one = {a.one}")
    print(f"b.four = {b.four}")

    print(f"a.name() = {a.name()}")
    print(f"b.name() = {b.name()}")
