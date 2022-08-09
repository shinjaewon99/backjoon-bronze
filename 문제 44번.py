# 1371번

n = int(input())

res = 0

for i in range(1, n+1):
    tmp = i+ sum(map(int,str(i)))


    if tmp == n:
        res = i 
        break

print(res)