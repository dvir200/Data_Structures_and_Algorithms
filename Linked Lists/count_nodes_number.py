class node:
  def __init__(self, data):
      self.data = data
      self.next = None

class Linked_List:
  def __init__(self):
    self.head = None

  def print_n_count(self):
    counter = 0
    tmp = self.head
    print(" Data entered in the list are :")
    while tmp:
      print("Data: " + str(tmp.data))
      counter = counter+1
      tmp = tmp.next
    print ("Number of nodes: " + str(counter))

if __name__=='__main__':

  Llist = Linked_List()

  Llist.head = node(5)
  second = node(9)
  third = node(33)

  Llist.head.next = second
  second.next = third

  Llist.print_n_count()