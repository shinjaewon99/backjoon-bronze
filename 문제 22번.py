# 1076번

color = ['black', 'brown', 'red', 
'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
a = color.index(input())
b = color.index(input())
c = color.index(input())
r = int(str(a) + str(b)) * (10 ** c)
print(r)