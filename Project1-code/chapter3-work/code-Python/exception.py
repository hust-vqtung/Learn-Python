def division(a, b):
    if(b==0):
        raise ZeroDivisionError("Division by zero!")
    else:
        return a/b

try:
    print(division(int(input()), int(input())))
except ZeroDivisionError as e:
    print(e)
