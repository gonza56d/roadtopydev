
class Climate:

    current = 'snow'

    #@staticmethod
    #def access():
    #    Climate.current = 'hehe'
    #    print(Climate.current)

    @classmethod
    def access(cls):
        cls.current = 'hehe'
        print(Climate.current)


Climate.access()
print(Climate.current)
