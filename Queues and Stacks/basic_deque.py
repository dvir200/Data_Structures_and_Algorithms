
""" deque - Module that is designed to work with queues and stacks """

""" import module from collections """
from collections import deque

queueStack = deque([])
print(queueStack)

""" Adding data in the beginning of the deque using append method"""
queueStack.append("data1")
queueStack.append(5)
print(queueStack)

""" Adding data in the beginning of the deque using appendleft method"""
queueStack.appendleft("tmp")
print(queueStack)

""" deleting data2 using pop method """
queueStack.pop()
print(queueStack)

""" deleting tmp using popleft method """
queueStack.popleft()
print(queueStack)