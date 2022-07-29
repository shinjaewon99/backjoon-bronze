# 1247번

from sys import stdin

for _ in range(3):
    n = int(stdin.readline())
    arr =[]
    for i in range(n):
        arr.append(int(stdin.readline()))
    if sum(arr)== 0:
        print('0')
    elif sum(arr)> 0 :
        print('+')
    else :
        print('-')