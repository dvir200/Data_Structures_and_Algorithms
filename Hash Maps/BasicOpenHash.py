""" Not Finished """
""" Person builder class """
class Person:
  def __init__(self, name, age, role):
      self.name = name
      self.age = age
      self.role = role

""" String to arr position converter """
def ExchangeToPos(name, ArrLength):
  result = 0
  for x in range(len(name)):
    result = result + ord(name[x])
  result = result % ArrLength
  return result


""" first try to build the insert function """
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


""" insert recursive function """
def insert(arr, pos, PersonObj):
  if arr[pos] is None:
    arr[pos] = PersonObj
    return arr
  else:
    try:
      return insert(arr, pos +1, PersonObj)
    except:
      pos = 0
      return insert(arr, pos, PersonObj) 

  

""" function that searches a person given a name and age. Uses searchCorrectPos function """
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
      result = arr[pos]
      print()
      print("Employee found:")
      print("Name: " + result.name)
      print("Age: " + str(result.age))
      print("Role: " + result.role)
      return
    else:
      print()
      print("Employee does not exist.")
      return


""" recursive function that helps the "search" and "delete" functions to find the right place in an array """
def searchCorrectPos(arr, index, personName, personAge, startingPos):
  if index == startingPos:
    return -1
  if ((arr[index].name == personName) & (arr[index].age == personAge)):
    """ print(index) """
    return index
  else:
    try:
      return searchCorrectPos(arr, index+1, personName, personAge, startingPos)
    except:
      index = 0
      return searchCorrectPos(arr, index, personName, personAge, startingPos)


""" function that deletes person credentials given his name and age. Uses searchCorrectPos function """
def delete(arr, personName, personAge):
  arrLength = len(arr)
  pos = ExchangeToPos(personName, arrLength)
  if ((arr[pos].name == personName) & (arr[pos].age == personAge)):
    arr[pos] = None
    print()
    print("Person info found and deleted.")
    return arr
  else:
    startingPos = pos
    pos = searchCorrectPos(arr, pos+1, personName, personAge, startingPos)
    if pos != -1:
      arr[pos] = None
      print()
      print("Person info found and deleted.")
      return arr
    else:
      print()
      print("No person info matches the given credentials.")
      return arr
  


""" main function that inserts a person object into an array """
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

  wanted = dataArr[0]
  print(wanted)
  print(wanted.name)
  print(wanted.age)
  print(wanted.role)

  search(dataArr, "Sebastian", 26)

  dataArr = delete(dataArr, "Sebastia", 31)

  wanted = dataArr[0]
  print(wanted)



