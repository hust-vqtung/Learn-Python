import math

a = float(input())
b = float(input())
c = float(input())
f = (a+b+c)/(a*a+b*b+1) - abs(a-(c*math.cos(b)))

print(f)