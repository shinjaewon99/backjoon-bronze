# 10808번


n = input()
list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
arr = [0]*26


for i in n:
	arr[list.index(i)] +=1

for j in arr:
    print(j , end= ' ')
