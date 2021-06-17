
class CapitalizedString:

    def __get__(self, instance, cls=None) -> str:
        return self.value

    def __set__(self, instance, value: str) -> None:
        if not isinstance(value, str):
            raise ValueError('Assigned value must be a string')
        self.value = value.capitalize()


class Person:

    name = CapitalizedString()


cleve = Person()
cleve.name = 'mauricio'
print(cleve.name)
