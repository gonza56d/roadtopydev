import ctypes


class Clase:
    pass


my_var = Clase()
my_var_address = id(my_var)

print(ctypes.c_long.from_address(my_var_address).value)
