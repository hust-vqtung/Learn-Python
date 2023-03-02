

n = int(input())
list = []

for i in range(n):
    list.append(int(input()))

for i in range(n-1):
    for j in range(n-i-1):
        if(list[j]>list[j+1]):
            list[j], list[j+1] = list[j+1], list[j]

for i in list:
    print(i, end=' ')