class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None

if __name__ == '__main__':

  root = node(5)
  root.left = node(4)
  root.right = node(6)

  print(str(root.data))
  print(str(root.left.data))
  print(str(root.right.data))