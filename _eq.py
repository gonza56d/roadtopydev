class Claze:
    
    def __init__(self) -> None:
        self.attr = 'hola'


class Clase:

    def __init__(self) -> None:
        self.attr = 'hola'

    def __eq__(self, o: object) -> bool:
        return hasattr(o, 'attr') and o.attr == self.attr


a = Clase()
a.attr = 'xd'
b = Claze()

print(a == b)
print(a is b)
