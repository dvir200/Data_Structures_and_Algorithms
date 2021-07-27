class node:
  def __init__(self, data):
      self.data = data
      self.next = None

class Circular_Linked_List:
  def __init__(self):
      self.head = None

  def insert(self, data):
    if (self.head == None):
      self.head = node(data)
      self.head.next = self.head
      return
    
    tmp = self.head
    while tmp.next != self.head:
      tmp = tmp.next

    new = node(data)
    tmp.next = new
    new.next = self.head
    return

  def display(self):
    tmp = self.head
    print(tmp.data)
    tmp = tmp.next
    while tmp != self.head:
      print(str(tmp.data))
      tmp = tmp.next


if __name__ == '__main__':

  user_circuler_list = Circular_Linked_List()

  for x in range (4):
    user_input = input()
    user_input = int(user_input)
    user_circuler_list.insert(user_input)

  print()
  print("Printing Circular Linked List:")
  user_circuler_list.display()