# 16199번



y , m , d = map(int,input().split())

y1 , m1 , d1 = map(int,input().split())


if m < m1 :
    year1 = y1 -y
elif m == m1 and d <= d1:
    year1 = y1 - y

else:
    year1 = y1 - y -1



year2 = y1-y +1

year3 = y1 - y

print(year1 , year2 ,year3 , sep="\n")