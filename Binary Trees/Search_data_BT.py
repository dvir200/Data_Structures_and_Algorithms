class node:
  def __init__(self,data):
    self.data = data
    self.left = None
    self.right = None

def search(node, key):
  if node is None:
    return 0
  
  if node.data == key:
    return 1

  else:
    check = search(node.left, key)

    if (check != 0):
      return check
    
    check = search(node.right, key)

    return check

if __name__ == '__main__':

  root = node(5)
  root.left = node(0)
  root.right = node(10)

  key = 3

  result = search(root, key)

  if result == 1:
    print("The data " + str(key) + " is in the binary tree")
  else:
    print("The data " + str(key) +" doesn't exist in the binary tree")
      