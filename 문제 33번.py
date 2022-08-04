# 13458번

n = int(input())

array = list(map(int,input().split()))

a,b = map(int,input().split())

count = n

for i in array:
    i -=a
    if i > 0:
        if i % b:
            count += (i//b) +1
        else :
            count += (i//b)

print(count)