

class Singleton:

    __shared_instance = None

    def __new__(cls):
        if cls.__shared_instance is not None:
            return cls.__shared_instance
        cls.__shared_instance = super().__new__(cls)
        return cls.__shared_instance


a = Singleton()
b = Singleton()
c = Singleton()
print(a is b is c)
