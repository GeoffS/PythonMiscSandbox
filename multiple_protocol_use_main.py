from typing import Protocol


class HasName(Protocol):
    def name(self): ...


class HasQuest(Protocol):
    def quest(self): ...


class HasNameAndQuest(HasName, HasQuest, Protocol): ...


# "Implements" the HasNameAndQuest protocol, but doesn't need to explicitly declare it.
# (but `mypy` will check for it!)
class NameAndQuest():
    def name(self): return "NameAndQuest.name()"
    def quest(self): return "NameAndQuest.quest()"


def needs_name_and_protocol(o: HasNameAndQuest) -> str:
    return f"needs_name_and_protocol: o.name()={o.name()}, o.quest()={o.quest()}"


if __name__ == '__main__':
    # `mypy` will complain if NameAndQuest doesn't have all the HasNameAndQuest methods.
    # Interestingly, pyCharm's static checker does complain...
    res = needs_name_and_protocol(NameAndQuest())

    print(res)