# 4766번

arr = []

while True:
    n = float(input())
    if n == 999:
        break

    arr.append(n)


for i in range(1,len(arr)):
    print("%.2f" % (arr[i] - arr[i-1]))