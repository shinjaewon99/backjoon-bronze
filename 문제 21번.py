# 3040번

from itertools import combinations


arr = []
for i in range(9):
    arr.append(int(input()))


impo = sum(arr) - 100


for com in combinations(arr,2):
    if sum(com) == impo:
        arr.remove(com[0])
        arr.remove(com[1])

for two in arr:
    print(two)