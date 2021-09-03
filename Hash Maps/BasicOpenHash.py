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
  if arr[pos] is True:
    while arr[pos] is not False:
      pos = pos +1
      """ if arr[pos] is None:
        pos = 0
      else:
        pos = pos +1 """
    arr[pos] = PersonObj
    return arr
  else:
    arr[pos] = PersonObj
    return arr


def main (arr, PersonObj):
  arrLength = len(arr)
  pos = ExchangeToPos(PersonObj.name, arrLength)
  insert(arr, pos, PersonObj)

if __name__ == '__main__':

  dataArr = [None, None, None, None, None, None, None, None, None, None]
  person1 = Person("Dvir", 18, "Developer")
  person2 = Person("Sebastian", 25, "Head of Marketing")
  main(dataArr, person1)
  main(dataArr, person2)

  wanted = dataArr[2]
  print()
  print(wanted.name)
  print(wanted.age)
  print(wanted.role)
