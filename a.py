from typing import Generator, List


def generate(l: List) -> Generator:
    yield from l


a = [1, 2, 3, 4, 5, 6, 7, 8]

gen = generate(a)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
