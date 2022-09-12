# 1526번

n = int(input())

while True:
    my = True

    for i in str(n):
        if i !="4" and i !="7":
            my = False
            n -=1

    if my:
        print(n)
        break