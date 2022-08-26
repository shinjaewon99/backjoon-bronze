# 14489번

n, m = map(int,input().split())


a = int(input()) * 2

total = n+m

if total - a >= 0 :
    print(total - a)

else:
    print(total)

