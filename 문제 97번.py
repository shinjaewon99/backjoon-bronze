# 1173번

N,m,M,T,R = map(int,input().split())

puzz = m
time = 0
play = 0

while play < N:
    if m+T > M:
        time = -1
        break
    time +=1

    if puzz + T <= M:
        puzz +=T
        play +=1
    else :
        if puzz -R < m:
            puzz = m
        else:
            puzz -= R

print(time)