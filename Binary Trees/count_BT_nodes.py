class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None

def count(root, counter = 1):
  if root is None:
    return
  else:
    count(root.left)
    count(root.right)
    counter = counter +1
  return counter




if __name__ == '__main__':

  root = node(5)
  root.left = node(4)
  root.right = node(3)

  print(str(count(root)))