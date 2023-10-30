s = "race a car"
ans = ""
for i in s:
  if ord(i) <97 and ord(i) > 64:
    j = ord(i) +32
    ans += chr(j)
  elif ord(i) < 65 and  ord(i) > 31:
    continue
  else:
    ans += i
tem = ans[::-1]


print(ans, tem)
if ans == tem:
  return True
else:
  print( False)   
