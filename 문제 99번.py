# 1673번

while 1:
    try:
        n, m = map(int, input().split())
        cnt = 0 
        cnt += n
        while n//m:
            cnt += n//m
            n = n//m + n%m
        print(cnt)
    except:
        break