""" node builder function """
class node:
  def __init__(self, name, age, role):
      self.name = name
      self.age = age
      self.role = role
      self.next = None


""" linked list class"""
class linkedList:
  """ basis for the linked list """
  def __init__(self):
      self.head = None
  
  """ inserts a node in a given arr position """
  def insertNode (self, name, age, role):
    if self.head == None:
      self.head = node(name, age, role)
      return self
    else:
      tmp = self.head
      prev = None
      while tmp:
        prev = tmp
        tmp = tmp.next
      prev.next = node(name, age, role)
      return self
  
  """ display the linked list in a given arr position """
  def display(self):
    tmp = self.head
    counter = 0
    while tmp:
      counter += 1
      print("Employee " + str(counter) + ":")
      print("Name: " + tmp.name)
      print("Age: " + str(tmp.age))
      print("Role: " + tmp.role)
      print()
      tmp = tmp.next
    return

""" function that will initilize all places in a array to be type of linked list object """
def initilize(arr, length):
  for x in range (len(arr)):
    arr[x] = linkedList()
  return arr

""" function that searches the array for the given name """
def search(arr, EmployeeName, EmployeeAge):
  pos = exchangeToPos(EmployeeName, len(arr))
  CurrentPos = arr[pos]
  if CurrentPos.head is None:
    print()
    print("Employee name not found")
  else:
    tmp = CurrentPos.head
    while tmp:
      if (tmp.name == EmployeeName) & (tmp.age == EmployeeAge):
        print()
        print("Credentials about employee " + str(EmployeeName) + " found:")
        print("Name: " + tmp.name)
        print("Age: " + str(tmp.age))
        print("Role: " + tmp.role)
        return
      tmp = tmp.next
    print()
    print("Employee name not found")


""" function that removes a node given the employee's name and age (for authentication) """
def removeNode(arr, EmployeeName, EmployeeAge):
  pos = exchangeToPos(EmployeeName, len(arr))
  CurrentPos = arr[pos]
  if CurrentPos.head is None:
    print()
    print("Employee name does not exist")
  else:
    tmp = CurrentPos.head
    prev = None
    while tmp:
      if (tmp.name == EmployeeName) & (tmp.age == EmployeeAge):
        if prev is None:
          CurrentPos.head = tmp.next
          """ tmp = None """
          print("Deletion Successful")
          return arr
        else:
          prev.next = tmp.next
          tmp = None
          print("Deletion Successful")
          return arr
      else:
        prev = tmp
        tmp = tmp.next
    print()
    print("Employee name does not exist")



""" exchange the name of the employee to a ASCII code """
def exchangeToPos(name, arrLength):
  result = 0
  for x in range(len(name)):
    result = result + ord(name[x])
  result = result % arrLength
  return result

""" main function that will automate anything """
def main(arr, name, age, role):
  pos = exchangeToPos(name, len(arr))
  arr[pos].insertNode(name, age, role)
  return dataArr


if __name__ == '__main__':

  dataArr = [None, None, None, None, None, None]
  print(len(dataArr))
  """ lengthArr = 6 """

  dataArr = initilize(dataArr, len(dataArr))

  dataArr = main(dataArr, "Zoe", 21, "Head of marketing team")
  """ wanted = dataArr[2]
  wanted.display() """
  dataArr = main(dataArr, "Sebastian", 34, "Head of IT team")
  dataArr = main(dataArr, "Sebastian", 25, "Developer")
  dataArr = main(dataArr, "Sebastian", 21, "Intern")
  dataArr = main(dataArr, "Romain", 34, "Head of Support")
  dataArr = main(dataArr, "Dvir", 25, "Developer")

  """ wanted = dataArr[2]
  wanted.display() """

  print()

  search(dataArr, "Marc", 50)

  print()
  removeNode(dataArr, "Sebastian", 26)

  wanted = dataArr[4]
  wanted.display()




