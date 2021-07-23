class node:
  def __init__(self, data) :
      self.data = data
      self.next = None

class linkedlist:
  def __init__(self):
      self.head = None

  def print(self):
    tmp = self.head
    while (tmp):
      print(tmp.data)
      tmp = tmp.next

if __name__=='__main__':

  linked = linkedlist()

  linked.head = node(1)
  second = node(2)
  third = node(3)

  linked.head.next = second
  second.next = third

  linked.print()
