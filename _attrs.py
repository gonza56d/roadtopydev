class Something:

    class_attr = 'clase'

    def __init__(self) -> None:
        self.instance_attr = 'instancia'


s = Something()
Something.class_attr = 'hola'
b = Something()
print(s.instance_attr)
print(b.instance_attr)
print(Something.class_attr)
