
from collections import deque


def add (self, data):
  self.append(data)
  return

if __name__ == '__main__':

  queueStack = deque([])
  add(queueStack, 5)
  add(queueStack, 9)
  add(queueStack, "data1")

  print(queueStack)

  queueStack.popleft()
  print(queueStack)