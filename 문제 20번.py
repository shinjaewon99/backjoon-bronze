# 2920번

a =list(map(int,input().split()))

if a == sorted(a):
    print("ascending")
elif a == sorted(a, reverse=True):
    print("descending")
else:
    print("mixed")