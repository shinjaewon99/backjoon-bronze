# 7567번


n = input()

cnt = 10

for i in range(1,len(n)):

    if n[i] == n[i-1]:
        cnt +=5

    else:
        cnt +=10

print(cnt)


