# 5063번

n = int(input())

for i in range(n):

    a,b,c = map(int,input().split())

    if a < b-c :
        print("advertise")

    elif a == b-c :
        print("does not matter")

    else : 
        print("do not advertise")


