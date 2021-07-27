class node:
  def __init__(self, data):
    self.data = data
    self.next = None
    self.prev = None

class Linked:
  def __init__(self):
        self.head = None

  def display(self):
    tmp = self.head
    while tmp:
      print(str(tmp.data))
      tmp = tmp.next


if __name__=='__main__':

  l_list = Linked()

  l_list.head = node(20)
  second = node(13)
  third = node(1)

  l_list.head.next = second
  second.prev = l_list.head

  second.next = third
  third.prev = second

  l_list.display()

  print("printing the prev node of the third node:")
  print(str(third.prev.data))
  