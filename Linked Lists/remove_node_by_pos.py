class node:
  def __init__(self, data):
      self.data = data
      self.next = None

class Linked_List:
  def __init__(self):
      self.head = None

  def remove (self, pos):
    tmp = self.head
    if pos ==1:
      self.head = tmp.next 
      tmp = None
      return
    else:
      counter = 1
    while tmp is not None:
      if counter == pos:
        prev.next = tmp.next
        tmp = None
        return
      counter = counter +1
      prev = tmp
      tmp = tmp.next
    
    if tmp is None:
      return


  def display(self):
    tmp = self.head
    while tmp:
      print (tmp.data)
      tmp = tmp.next


if __name__=='__main__':

  linked = Linked_List()

  linked.head = node(33)
  second = node(5)
  third = node(63)
  fourth = node(2)

  linked.head.next = second
  second.next = third
  third.next = fourth

  print("Before:")

  linked.display()

  delete = 5

  linked.remove(delete)

  print()
  print("After:")

  linked.display()

