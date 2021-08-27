class node:
  def __init__(self, data):
      self.data = data
      self.next = None

class LinkedList:
  def __init__(self):
      self.head = None

  def insert (self, data):
    if self.head == None:
      self.head = node(data)
      return
    else:
      tmp = self.head
      prev = None
      while tmp:
        prev = tmp
        tmp = tmp.next
      prev.next = node(data)
      return

  def display(self):
    tmp = self.head
    while tmp:
      print(tmp.data)
      tmp = tmp.next
    return


arr = [None, None]
print(len(arr))

arr[0] = LinkedList()
arr[1] = LinkedList()

arr[0].insert(10)
arr[1].insert(5)

tmp = arr[0]
tmp.display()

tmp = arr[1]
tmp.display()

