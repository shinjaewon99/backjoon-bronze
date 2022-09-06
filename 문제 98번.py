# 1350번

n = int(input())
m = list(map(int,input().split()))

arr = input()
sum = 0
for i in m:
    if i % arr == 0 :
        sum += i//arr
    else:
        sum += i//arr+1
print(sum * arr)

