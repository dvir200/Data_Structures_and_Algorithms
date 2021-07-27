class node:
  def __init__(self, data):
    self.data = data
    self.next = None
    self.prev = None

class Linked_List:
  def __init__(self):
    self.head = None

  def insert(self,data):
    if (self.head == None):
      self.head = node(data)
      return
    tmp = self.head
    while tmp.next:
      tmp = tmp.next

    tmp.next = node(data)
    tmp.next.prev = tmp
    return

  def display(self):
    tmp = self.head
    while tmp:
      print(str(tmp.data))
      tmp = tmp.next

if __name__ == '__main__':

  new_linked = Linked_List()

  for x in range(4):
    user_input = input()
    user_input = int(user_input)
    new_linked.insert(user_input)

  print()
  print("Printing:")
  new_linked.display()