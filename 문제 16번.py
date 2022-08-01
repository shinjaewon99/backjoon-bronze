# 1159번


from collections import Counter


n = int(input())
player = []
arr =[]

cnt =0

for i in range(n):
    m = input()
    player.append(m[0])
player_count = Counter(player)

for i,j in player_count.items():

    if j >= 5:
        arr.append(i)
        cnt +=1

arr.sort()

if cnt== 0:
    print("PREDAJA")

else:
    for i in arr:
        print(i,end='')


 