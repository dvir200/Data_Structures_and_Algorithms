class node:
  def __init__(self, data):
      self.data = data
      self.next = None

class Linked_list:
  def __init__(self):
      self.head = None

  def insert_loop(self, data):
    if self.head == None:
      self.head = node(data)
      return 
    tmp = self.head
    while (tmp.next != None):
      tmp = tmp.next
    
    tmp.next = node(data)
    return

  def display(self):
    tmp = self.head
    while tmp:
      print(tmp.data)
      tmp = tmp.next

if __name__=='__main__':

  linked = Linked_list()

  for x in range(5):
    user_input = input()
    user_input = int(user_input)
    linked.insert_loop(user_input)

  print()
  print("Printing Values:")
  linked.display()