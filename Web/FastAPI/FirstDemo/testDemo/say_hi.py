from typing import Optional


class Person:
    def __init__(self, name: str):
        self.name = name


def say_hi(name: Optional[str] = None):
    if name is not None:
        print(f'Hey {name}!')
    else:
        print('hello world')


def get_person_name(one_person: Person):
    return one_person.name
