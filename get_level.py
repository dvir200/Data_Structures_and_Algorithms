class node:
  def __init__(self,data):
      self.data = data
      self.left = None
      self.right = None

def get_level(node, key, level=1):
  if node is None:
    return 0
  
  if node.data == key:
    return level

  else:
    downlevel = get_level(node.left, key, level +1)
    if downlevel != 0:
      return downlevel

    downlevel = get_level(node.right, key, level +1)

    return downlevel


if __name__ == '__main__':

  root = node(5)
  root.left = node(3)
  root.right = node(1)
  root.left.left = node(4)
  root.left.right = node(10)

  key = 10

  result = str(get_level(root, key))

  print ("level of " + str(key) + " is: " + str(result))