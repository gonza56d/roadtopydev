
class CapitalizedString:

    def __get__(self, instance, cls=None) -> str:
        return self.value

    def __set__(self, instance, value: str) -> None:
        if not isinstance(value, str):
            raise ValueError('Assigned value must be a string')
        self.value = value.capitalize()


class Person:

    name = CapitalizedString()

    def __init__(self, name: str) -> None:
        self.name = name


person = Person('gonza')
p2 = Person('alguien')
print(p2.name)
print(person.name)
print(person.__dict__)
