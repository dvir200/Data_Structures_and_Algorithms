from collections import deque

def addToStack(string, userStack):
  for x in range (len(string)):
    userStack.append(string[x])
  return

def reverse(userStack):
  newString = ""
  while userStack:
    newString = newString + userStack.pop()
  print(newString)



string1 = "samsung"

""" Output: gnusmas """

stack = deque([])
addToStack(string1, stack)
reverse(stack)