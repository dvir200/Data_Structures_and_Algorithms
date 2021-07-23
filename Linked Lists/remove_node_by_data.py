class node:
  def __init__(self, data):
      self.data = data
      self.next = None

class Linked_List:
  def __init__(self):
      self.head = None

  def remove(self, info):
    tmp = self.head
    if (self.head.data == info):
      self.head = tmp.next
      return True

    while tmp is not None:
      if (tmp.data == info):
        prev.next = tmp.next
        tmp = None
        return True
      prev = tmp
      tmp = tmp.next

    if tmp is None:
      return False

  def display (self):
    tmp = self.head
    while tmp:
      print(tmp.data)
      tmp = tmp.next

if __name__=='__main__':

  linked = Linked_List()

  linked.head = node(50)
  second = node(1)
  third = node(22)

  linked.head.next = second
  second.next = third

  print("Before:")
  linked.display()
  print()
  print("After:")

  Linked_Data = 10

  if linked.remove(Linked_Data):
    print("Data Found And Deleted")
    linked.display()
  else:
    print("Data does not exist")