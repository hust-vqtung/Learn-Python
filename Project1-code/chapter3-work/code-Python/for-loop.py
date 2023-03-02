

n = int(input())
numList = []

for i in range(n+1):
    numList.append(1)

for i in range(2, n+1):
    for j in range(2, n//i+1):
        numList[i*j] = 0

for i in range(2, n+1):
    if(numList[i]==1):
        print(i, end=' ')
