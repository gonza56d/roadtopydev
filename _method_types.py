
class Climate:

    current = 'snow'

    @classmethod
    def whatever(cls):
        pass

    @staticmethod
    def access():
        Climate.current = 'clima'
        print(Climate.current)

    @classmethod
    def access(cls):
        cls.current = 'hehe'
        print(Climate.current)


class Dummy(Climate):
    pass


d = Dummy()
print(dir(Dummy))


#Climate.access()
#print(Climate.current)
