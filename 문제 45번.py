# 1264번


while True:
    tmp = input()

    if tmp =='#':
        break

    val = ['a','e','i','o','u','A', 'E', 'I', 'O', 'U']

    res = 0

    for i in range(len(tmp)):
        if tmp[i] in val:
            res += 1


    print(res)
    