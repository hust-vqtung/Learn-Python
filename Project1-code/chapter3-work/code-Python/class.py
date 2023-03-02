import math

class Toado:
    def __init__(self, ten, x, y, z):
        self.ten = ten
        self.x = x
        self.y = y
        self.z = z

t1 = Toado(input(), int(input()),
           int(input()), int(input()))
print("{ten}({x},{y},{z})" \
      .format(ten=t1.ten, x=t1.x, y=t1.y, z=t1.z))

t2 = Toado(input(), int(input()),
           int(input()), int(input()))
print("{ten}({x},{y},{z})" \
      .format(ten=t2.ten, x=t2.x, y=t2.y, z=t2.z))

print(math.sqrt((t1.x-t2.x)*(t1.x-t2.x)
        + (t1.y-t2.y)*(t1.y-t2.y)
        + (t1.z-t2.z)*(t1.z-t2.z)))