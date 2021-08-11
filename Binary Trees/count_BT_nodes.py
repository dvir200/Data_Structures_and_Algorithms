class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None



def count(root):
  if root is None:
    return 0
  else:
    return 1 + count(root.left) + count(root.right)
    



if __name__ == '__main__':

  root = node(5)
  root.left = node(4)
  root.right = node(3)

  print(str(count(root)))