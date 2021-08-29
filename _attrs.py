class Attr:
    pass


class Something:

    class_attr = Attr()

    def __init__(self) -> None:
        self.instance_attr = 0


s = Something()
s.class_attr = 'hola'
b = Something()
print(type(s.class_attr))
print(type(b.class_attr))
print(type(Something.class_attr))
