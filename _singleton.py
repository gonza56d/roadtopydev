

class Singleton:

    __shared_instance = None

    @staticmethod
    def get_instance():
        if Singleton.__shared_instance is None:
            Singleton()
        return Singleton.__shared_instance

    def __init__(self) -> None:
        if Singleton.__shared_instance is not None:
            raise Exception('This is a singleton class.')
        Singleton.__shared_instance = self


a = Singleton.get_instance()
b = Singleton.get_instance()
c = Singleton.get_instance()
print(id(a), id(b), id(c))
