
# 1453번 

n = int(input())

cos = list(map(int,input().split()))

count = 0

seat = []

for j in range(n):
    if cos[j] in seat:
        count += 1

    else :
        seat.append(cos[j])

print(count)
