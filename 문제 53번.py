# 3460번

n = int(input())

for i in range(n) :
  a = bin(int(input()))[2:]
  
  for j in range(len(a)) :
    if a[::-1][j] == '1' :
      print(j, end=' ')

