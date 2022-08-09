# 2309번

arr = []

for i in range(9):
    arr.append(int(input()))

sum_arr = sum(arr)

a = 0
b = 0

for i in range(8):
    for j in range(i+1 , 9):
        if sum_arr - (arr[i] + arr[j]) == 100:
            a = arr[i]
            b = arr[j]
arr.remove(a)
arr.remove(b)

arr.sort()

for i in arr:
    print(i)

