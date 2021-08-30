

class Person:

    def __init__(self) -> None:
        self.__name = ''

    @property
    def name(self) -> str:
        return self.__name
    
    @name.setter
    def name(self, value: str):
        if not isinstance(value, str):
            raise ValueError('Name value must be str')
        self.__name = value.capitalize()


person = Person()
person.name = 'gonza'
print(person.name)
