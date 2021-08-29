
class Borg:

    __shared_state = {}

    def __init__(self):
        self.__dict__ = self.__shared_state


a = Borg()
a.comida_favorita = 'milanesa'
print(id(Borg._Borg__shared_state))
print(id(a._Borg__shared_state))
b = Borg()
print(b.comida_favorita)
