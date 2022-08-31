# 2566번

arr = []

for i in range(9):
    arr.append(list(map(int,input().split())))


a = 0
b = 0


max = -1

for j in range(9):
    for k in range(9):
        if arr[j][k] > max:
            max = arr[j][k]

            a = j+1
            b = k+1


print(max)
print(a,b)