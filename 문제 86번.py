# 2991번

a,b,c,d = map(int,input().split())


arr = list(map(int,input().split()))

for i in arr :
    cnt = 0
    if 0 < i % (a+b) <= a: cnt +=1
    if 0 < i % (c+d) <= c: cnt +=1

    print(cnt)