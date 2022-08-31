# 2875번

a,b,c = map(int,input().split())

cnt = 0

while a+b >= c and a >= 0 and b >=0:
    a -=2
    b -=1
    cnt +=1

print(cnt-1)