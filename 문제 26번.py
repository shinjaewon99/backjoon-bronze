# 3460번

n = int(input())

for _ in range(n):
    a = bin(int(input()))[2:]
    for j in range(len(n)):
        if n[-j-1] == '1':
            print(j, end = " ")