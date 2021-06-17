
class Borg:

    _shared_state = {}

    def __init__(self) -> None:
        self.__dict__ = self._shared_state


class Corg(Borg):
    pass


class Dorg(Borg):
    pass


a = Corg()
a.queso = 'rico'
print(id(a._shared_state))
print(id(a.__dict__))
b = Dorg()
print(b.queso)

print(id(b._shared_state))
print(id(b.__dict__))
