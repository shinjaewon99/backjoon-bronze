# 9325번




n = int(input())

for i in range(n):
    a = int(input())
    b = int(input())

    price = a

    for j in range(b):
        q, p = map(int,input().split())

        price += q*p

    print(price)