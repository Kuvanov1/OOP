import math
class Vektor_XY:
    def __init__(self, x1, x2, y1, y2, z1, z2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.z1 = z1
        self.z2 = z2

class Vektor2_3D(Vektor_XY):

    def qoshish(self):
        x3 = self.x2 + self.x1
        y3 = self.x2 + self.x1
        z3 = self.z2 + self.z1
        return f"A + B = ({x3},{y3},{z3})"

    def ayirish(self):
        x3 = self.x2 - self.x1
        y3 = self.y2 - self.y1
        z3 = self.z2 - self.z1
        x4 = self.x1 - self.x2
        y4 = self.y1 - self.y2
        z4 = self.z1 - self.z2
        return f"B - A = ({x3},{y3},{z3}) or A - B = ({x4},{y4},{z4})"

    def uzunligi(self):
        uzunlik = math.sqrt((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2 + (self.z2 - self.z1) ** 2)
        return uzunlik

    def skalyar_kopaytma(self):
        kopaytma = self.x1 * self.x2 + self.y1 * self.y2 +self.z1 * self.z2
        return kopaytma

    def burchak(self):
        maxraj = math.sqrt(x1 ** 2 + y1 ** 2 + z1 ** 2) * math.sqrt(x2 ** 2 + y2 ** 2 + z2 ** 2)
        kopaytma = self.x1 * self.x2 + self.y1 * self.y2 + self.z1 * self.z2
        return kopaytma / maxraj



x1 = int(input("x1: "))
x2 = int(input("x2: "))
y1 = int(input("y1: "))
y2 = int(input("y2: "))
z1 = int(input("z1: "))
z2 = int(input("z1: "))

calculate = Vektor2_3D
print(calculate.qoshish)

