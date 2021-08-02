"""Last in, first out."""

from collections import deque


stack = deque()
stack.append(123)
stack.append(392)
stack.append(69)
print(stack.pop())
print(stack.pop())
