class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None


def display_InOrder(root):
  if root is None:
    return None
  else:
    display_InOrder(root.left)
    print(str(root.data))
    display_InOrder(root.right)
    return

if __name__ == '__main__':

  root = node(1)
  root.left = node(2)
  root.right = node(3)
  root.left.left = node(4)
  root.left.right = node(5)

  display_InOrder(root)