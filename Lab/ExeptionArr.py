

arr = [1, 2, 3, 4, 5]
""" Arr length =  5"""

""" following line brings IndexError """
""" print(arr[6]) """


""" try:
  print(arr[6])
except:
  print("Not valid position") """

if arr[6] == IndexError:
  print("Index Error")