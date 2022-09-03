# 5523번

n = int(input())

a = 0
b = 0
for i in range(n):

    x,y = map(int,input().split())

    if a > b :
        a +=1
    elif b < a:
        b += 1


print(a,b)





