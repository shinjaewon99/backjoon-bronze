# 1267번

n = int(input())
m = list(map(int,input().split()))


ys = 0

ms = 0

for i in m :
    ys += i//30 *10 + 10
    ms += i//60 * 15 + 15

if ys > ms:
    print("M" , ms)
elif ms > ys:
    print("Y" , ys)

else:
    print("Y" , "M" , ys)