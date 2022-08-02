# 1252번 

n , m = input().split()

n = int(n,2)

m = int(m,2)

tot = bin(n+m)[2:]

print(tot)