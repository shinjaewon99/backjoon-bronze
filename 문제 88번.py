# 4504번




n = int(input())

while True :
  a = int(input())
  if a == 0 :
    break
  if a % n == 0 :
    print(str(a) + " is a multiple of " + str(n)+".")
  else :
    print(str(a) + " is NOT a multiple of " + str(n)+".")
