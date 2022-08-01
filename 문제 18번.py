# 1977번

n = int(input())

m = int(input())

arr = []

i = 1

while i ** 2 <= m:
    if n <= i ** 2 <= m:

        arr.append(i**2)
    i +=1

if arr ==[]:
    print(-1)

else :
    print (sum(arr))

    print (arr[0])
    