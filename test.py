
class StrictInt:

    def __init__(self) -> None:
        self.value = None
    
    def __get__(self, value, type=None) -> int:
        return self.value

    def __set__(self, obj, value: int) -> None:
        if not isinstance(value, int):
            raise ValueError('Only int values can be set to StrictInt attribute.')
        self.value = value


class UppercasedStr:

    def __init__(self) -> None:
        self.value = ''

    def __get__(self, value, type=None) -> str:
        return self.value

    def __set__(self, obj, value: str) -> None:
        if not isinstance(value, str):
            raise ValueError('Only str values can be set to UppercasedStr attribute.')
        self.value = value.upper()


class Person:

    first_name = UppercasedStr()
    last_name = UppercasedStr()
    dni = StrictInt()


gonza = Person()
gonza.first_name = 'gonza'
gonza.dni = 'hola'
print(gonza.first_name)
print(gonza.dni)
