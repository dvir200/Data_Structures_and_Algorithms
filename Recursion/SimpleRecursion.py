def SimpleRec(n):
  if n ==0:
    return 0
  else:
    return n+ SimpleRec(n-1)


print(SimpleRec(10))