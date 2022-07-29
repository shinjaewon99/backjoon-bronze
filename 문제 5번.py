# 1284번

while True:
    arr = []
    n = input()
    if n == '0':
        break
    for i in n:
        arr.append(i)

    total = 0
    for i in arr:
        total += 1
        if i == '0':
            total += 4
        elif i == '1':
            total += 2
        else:
            total += 3
    total += 1
    print(total)


