class node:
  def __init__(self, data):
      self.data = data
      self.next = None

class linked_list:
  def __init__(self):
      self.head = None

  def sort(self, data):
    if (self.head == None):
      self.head = node(data)
      return
    if (data < self.head.data):
      new = node(data)
      save_head = self.head
      save_next = self.head.next
      self.head = new
      new.next = save_head
      save_head.next = save_next
      return

    tmp = self.head
    prev = None
    while tmp:
      if (data< tmp.data):
        new = node(data)
        prev.next = new
        new.next = tmp
        return
      else:
        prev = tmp
        tmp = tmp.next

    prev.next = node(data)
    return

  def display(self):
    tmp = self.head
    while tmp:
      print(str(tmp.data))
      tmp = tmp.next


if __name__ == '__main__':
  user_list = linked_list()
  for x in range(4):
    user_input = input()
    user_input = int(user_input)
    user_list.sort(user_input)

  print()
  print("Printing List:")
  user_list.display()