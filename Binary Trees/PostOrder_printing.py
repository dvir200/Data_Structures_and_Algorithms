class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None


def display_PostOrder(root):
  if root is None:
    return None
  else:
    display_PostOrder(root.left)
    display_PostOrder(root.right)
    print(str(root.data))
    return

if __name__ == '__main__':

  root = node(1)
  root.left = node(2)
  root.right = node(3)
  root.left.left = node(4)
  root.left.right = node(5)



  display_PostOrder(root)