def reverse (a, length  ,rev=""):
  if length<0:
    return rev
  else:
    rev = rev + a[length]
    return reverse(a, length-1, rev)


word = "mama"
print(reverse(word, len(word)-1))