
#1075번

n = input()
m = int(input())

arr = int(n[:-2] + '00')

while True:
    if arr % m ==0 :
        break

    arr +=1

print(str(arr)[-2:])
