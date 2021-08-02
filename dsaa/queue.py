"""First in, first out."""

# You can use list, however it's not recommended

stock_price_queue = []
stock_price_queue.insert(0, 132)
stock_price_queue.insert(0, 115)
stock_price_queue.insert(0, 195)
print(stock_price_queue.pop())
print(stock_price_queue.pop())
print(stock_price_queue)

# deque is better

from collections import deque


q = deque()
q.appendleft(132)
q.appendleft(115)
q.appendleft(195)
print(q.pop())
print(q.pop())
print(q.pop())

