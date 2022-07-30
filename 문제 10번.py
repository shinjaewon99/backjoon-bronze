# 10101번

a = int(input())
b = int(input())
c = int(input())

cnt = 0

if a == b == c == 60 :
  print("Equilateral")
elif a + b + c != 180 :
  print("Error")
else :
  if a == b :
   cnt += 2
  elif a == c :
    cnt += 2
  elif b == c :
    cnt += 2

  if cnt >= 2 :
    print("Isosceles")
  else :
    print("Scalene")