
class Singleton:

    __shared_instance = None

    def __new__(cls):
        if Singleton.__shared_instance is None:
            Singleton.__shared_instance = object.__new__(cls)
        return Singleton.__shared_instance
        


a = Singleton()
b = Singleton()
print(id(a), id(b))
