# 11948번

sum = 0

arr = []

for i in range(4):
    arr.append(int(input()))


arr.sort()

for j in range(1,4):
    sum +=arr[j]


brr = []

for _ in range(2):
    brr.append(int(input()))

brr.sort()

sum +=brr[1]

print(sum)


