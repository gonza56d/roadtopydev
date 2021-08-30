import ctypes


class Singleton:

    __shared_instance = None

    def __new__(cls):
        if cls.__shared_instance is None:
            cls.__shared_instance = super().__new__(cls)
        return cls.__shared_instance


a = Singleton()
b = Singleton()
c = Singleton()
print(a is b is c)
del b
print(a is c)
print(type(Singleton))

my_var_address = id(Singleton._Singleton__shared_instance)

print(ctypes.c_long.from_address(my_var_address).value)
