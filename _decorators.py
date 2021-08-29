import functools


def greets(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('Hi!')
        value = func(*args, **kwargs)
        print(value)
        print('Bye!')
        return value
    return wrapper



@greets
def something():
    return 'xd'


print(something())
