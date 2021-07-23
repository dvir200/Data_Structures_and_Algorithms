def palindrome(a, descender, climber=0):
  if (a[climber] != a[descender]):
    return False
  if climber> descender:
    return True
  if climber==descender:
    return True
  else:
    return palindrome(a, descender-1, climber+1)

UserString= "geeks"
check = palindrome(UserString, len(UserString)-1)
if check:
  print("Word is palindrome")
else:
  print("Word is not palindrome")