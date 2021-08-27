""" node builder function """
class node:
  def __init__(self, name, age, role):
      self.name = name
      self.age = age
      self.role = role
      self.next = None


""" basis for the linked list """
class linkedList:
  def __init__(self):
      self.head = None
  
  """ inserts a node in a given arr position """
  def insertNode (self, name, age, role):
    if self.head == None:
      self.head = node(name, age, role)
      return
    else:
      tmp = self.head
      prev = None
      while tmp:
        prev = tmp
        tmp = tmp.next
      prev.next = node(name, age, role)
      return
  
  """ display the linked list in a given arr position """
  def display(self):
    tmp = self.head
    while tmp:
      print(tmp.data)
      tmp = tmp.next
    return

""" function that will initilize all places in a array to be type of linked list object """
def initilize(arr, length):
  for x in range (len(arr)):
    arr[x] = linkedList()
  return arr


""" exchange the name of the employee to a ASCII code """
def exchangeToPos(name, arrLength):
  result = 0
  for x in range(len(name)):
    result = result + ord(name[x])
  result = result % arrLength
  return result

""" main function that will automate anything """
def main(arr, name, age, role):
  arr = initilize(arr, len(arr)-1)
  pos = exchangeToPos(name, len(arr))
  arr[pos].insertNode(name, age, role)
  return


if __name__ == '__main__':

  dataArr = [None, None, None, None, None, None]
  print(len(dataArr))
  """ lengthArr = 6 """

  dataArr = main(dataArr, "Zoe", 21, "Head of marketing team")
  dataArr = main(dataArr, "Sebastian", 34, "Head of IT team")


