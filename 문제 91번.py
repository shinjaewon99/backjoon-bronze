# 5361번




n = int(input())

arr = [350.34, 230.90, 190.55, 125.30, 180.90]

for i in range(n):
    sum = 0

    data = list(map(float,input().split()))

    for j in range(5):

        sum += arr[j] * data[j]


    print("$%.2f" % sum)

