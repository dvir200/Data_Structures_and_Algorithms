class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None

def display(root):
  if root is None:
    return None
  else:
    print(str(root.data))
    display(root.left)
    display(root.right)
    return

if __name__ == '__main__':

  root = node(6)
  root.left = node(7)
  root.right = node(8)
  root.left.left = node(10)
  root.left.right = node(11)
  root.right.right = node(5)
  root.right.left = node(1)

  """ print(str(root.data))
  print(str(root.left.data))
  print(str(root.right.data)) """

  display(root)
 