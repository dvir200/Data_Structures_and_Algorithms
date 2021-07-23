def ways(a, index=0):
  if a<=0:
    return
  else:
    print(str(a) + ("+1")*index)
    return ways(a-1, index+1)


num = 3
ways(num)