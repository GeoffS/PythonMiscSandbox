from typing import Callable

HasName = Callable[[int], str]

def needs_named_thing(f: HasName) -> str:
    i: int = 2
    return f"needs_named_thing f({i}) = {f(i)}"


def is_named_thing(i: int) -> str: # HasName type-alias impl...
    return f"is_named_thing({i})"


if __name__ == '__main__':
    print(needs_named_thing(is_named_thing))