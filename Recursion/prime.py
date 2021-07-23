def isPrime (n, index=2):
  if (n%index == 0):
    return False
  if (index == n-1):
    return True
  else:
    return isPrime(n, index+1)

num = 7
if isPrime(num):
  print("Number is prime")
else:
  print("Number is not prime")