class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None

def add_by_order(root, data):
  """ if root is None:
    root = node(data)
    return """

  if (root.data == data):
    print("data already exists")
    return
  
  if (data > root.data):
    if root.right is None:
      root.right = node(data)
    else:
      add_by_order(root.right, data)

  if (data < root.data):
    if root.left is None:
      root.left = node(data)
    else:
      add_by_order(root.left, data)

def display(root):
  if root is None:
    return None
  else:
    print(str(root.data))
    display(root.left)
    display(root.right)
    return

if __name__ == '__main__':

  root = node(5)

  for x in range(6):
    num = input()
    num = int(num)
    add_by_order(root ,num)

  print()
  print("Printing BST:")
  display(root)