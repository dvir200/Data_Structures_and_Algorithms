""" Not Finished """

class Person:
  def __init__(self, name, age, role):
      self.name = name
      self.age = age
      self.role = role

def ExchangeToPos(name, ArrLength):
  result = 0
  for x in range(len(name)):
    result = result + ord(name[x])
  result = result % ArrLength
  return result


def insert(arr, pos, PersonObj):
  if arr[pos] is None:
    arr[pos] = PersonObj
    return arr
  else:
    try:
      insert(arr, pos +1, PersonObj)
    except:
      pos = 0
      insert(arr, pos, PersonObj) 
  
def searchCorrectPos(arr, pos, personName, personAge, startingPos):
  if ((arr[pos].name == personName) & (arr[pos].age == personAge)):
    return pos
  if pos == startingPos:
    return -1
  else:
    try:
      searchCorrectPos(arr, pos+1, personName, personAge, startingPos)
    except:
      pos = 0
      searchCorrectPos(arr, pos, personName, personAge, startingPos)
  

""" def insert(arr, pos, PersonObj):
  if arr[pos] is True:
    while arr[pos] is not None:
      if arr[pos +1] == IndexError:
        pos = 0
      else:
        pos = pos +1
    arr[pos] = PersonObj
    return arr
  else:
    arr[pos] = PersonObj
    return arr """

def search (arr, personName, personAge):
  arrLength = len(arr)
  pos = ExchangeToPos(personName, arrLength)
  if ((arr[pos].name == personName) & (arr[pos].age == personAge)):
    print()
    print("Employee found:")
    print("Name: " + arr[pos].name)
    print("Age: " + str(arr[pos].age))
    print("Role: " + arr[pos].role)
    return
  else:
    startingPos = pos
    pos = searchCorrectPos(arr, pos+1, personName, personAge, startingPos)
    if pos != -1:
      print()
      print("Employee found:")
      print("Name: " + arr[pos].name)
      print("Age: " + str(arr[pos].age))
      print("Role: " + arr[pos].role)
      return
    else:
      print()
      print("Employee does not exist.")
      return


  


def main (arr, PersonObj):
  arrLength = len(arr)
  pos = ExchangeToPos(PersonObj.name, arrLength)
  insert(arr, pos, PersonObj)

if __name__ == '__main__':

  dataArr = [None, None, None, None]
  person1 = Person("Dvir", 18, "Developer")
  person2 = Person("Sebastian", 25, "Head of Marketing")
  person3 = Person("Sebastian", 26, "Head of support")
  person4 = Person("Sebastian", 31, "Developer")
  main(dataArr, person1)
  main(dataArr, person2)
  main(dataArr, person3)
  main(dataArr, person4)

  wanted = dataArr[3]
  print(wanted)
  print(wanted.name)
  print(wanted.age)
  print(wanted.role)

  search(dataArr, "Sebastian", 31)


