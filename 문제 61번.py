# 9093번

for i in range(int(input())):
    a = input().split()
    for j in a:
        print(j[::-1], end=' ')
    print()