# 1357번


n,m = map(str,input().split())

s = str(int(n[::-1])+ int(m[::-1]))

print(int(s[::-1]))
