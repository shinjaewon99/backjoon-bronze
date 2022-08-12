# 2851번


arr = []
total = 0

for i in range(10):
    arr.append(int(input()))

for j in arr:
    total +=j

    if total >= 100:
        if total -100 > 100 - (total-j):
            total -=j
            break

print(total)