def pow(a, b):
    if(b==0):
        return 1
    else:
        res = 1
        while(b!=0):
            res *= a
            b = b - 1
        return res

n = int(input())
x = float(input())
i = 1
sum = 0

while(i<=n):
    sum += pow(-1, i-1)*pow(x, i)
    i = i + 1

print(sum)
