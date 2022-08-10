# 2460번


res = 0
n = 0

for i in range(10):
    a,b = map(int,input().split())

    n -=a
    n +=b

    res = max(res, n)

print(res)