import math

a = float(input())
b = float(input())
c = float(input())
delta = b*b - 4*a*c

if (a==0 and b!=0):
    print(-c/b)
    quit()

elif (a==0 and b==0 and c==0):
    print("Phuong trinh vo so nghiem")
    quit()

elif (a==0 and b==0 and c!=0):
    print("Phuong trinh vo nghiem")
    quit()
        
if (delta<0):
    print(-b/(2*a), '+', '{}i'.format(math.sqrt(abs(delta))/(2*a)))
    print(-b/(2*a), '-', '{}i'.format(math.sqrt(abs(delta))/(2*a)))
    
elif (delta>0):
        print(-b/(2*a)+math.sqrt(abs(delta))/(2*a))
        print(-b/(2*a)-math.sqrt(abs(delta))/(2*a))
    
else:
        print(-b/(2*a)+math.sqrt(abs(delta))/(2*a))