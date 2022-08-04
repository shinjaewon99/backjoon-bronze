# 10093번

n,m=map(int,input().split())
a   =   min(n,m)
b   =   max(n,m)
if(n==m):
    print(0)
else:
    print(b-a-1)
    for i in range(a+1,b):
        print(i,end=' ')