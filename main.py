import types


class Thingy():
    pass

def thingy_method(self) -> str:
    return f"thingy_method: {self}"


if __name__ == '__main__':
    a = Thingy()
    a.one = 1
    a.two = 2
    a_thingy_method = types.MethodType( thingy_method, a )
    print(f"a_thingy_method = {a_thingy_method}")
    print(f"a_thingy_method() = {a_thingy_method()}")
    a.name = a_thingy_method

    b = Thingy()
    b.three = 3
    b.four = 4
    b_lambda = types.MethodType( lambda self: f"b_lambda: {self}", b)
    b.name = b_lambda

    print(f"a.one = {a.one}")
    print(f"b.four = {b.four}")

    print(f"a.name() = {a.name()}")
    print(f"b.name() = {b.name()}")