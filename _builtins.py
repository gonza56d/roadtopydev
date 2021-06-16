"""Python builtin types."""

# boolean
bool            # True or False

# Text, and it's an iterable
str             # 'Hello'

# Numeric
int             # 6   
float           # 6.36
complex         # 1j

# sequence
list            # ['a', 'x', 4, 4, 0] ordered and admits changes
tuple           # (4, 7, 'a')         ordered and does not admit changes
range           # range(3, 9)         will have every value from 3 to 8

# mapping
dict            # {'a': 1, 'b': (1, 4)}     key-value thing

# Set
set             # {1, 2, 3, 3}        unordered, set of non-repeated values, will end having {1, 2, 3}
frozenset       # {1, 2, 3, 3}        unordered, set of non-repeated values, will end having {1, 2, 3} and can't change

# binary
bytes, bytearray, memoryview
