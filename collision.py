from cmath import sqrt
import re

def clamp(x, left, right):
    return max(min(x, right), left)

class Vec:
    def __init__(self, x = None, y = None):
        self.x = x
        self.y = y

    def len(self):
        return sqrt(self.x * self.x + self.y * self.y)
    
    def len2(self):
        return self.x * self.x + self.y * self.y

    def __neg__(self):
        return Vec(-self.x, -self.y)

    def __add__(self, other):
        return Vec(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vec(self.x - other.x, self.y - other.y)

    def __mul__(self, a):
        return Vec(a * self.x, a * self.y)
    
    def __rmul__(self, a):
        return Vec(a * self.x, a * self.y)

    def __truediv__(self, a):
        return Vec(self.x / a, self.y / a)

class Circle:
    def __init__(self, x = 1, y = 1, r = 1):
        self.pos = Vec(x, y)
        self.r = r

def collision_cc(circle1, circle2):
    d = circle1.pos - circle2.pos
    r = circle1.r - circle2.r
    
    return d.len2() < r**2



def testare_coordonate(coordx, coordy):
    try:
        coords_x = float(coordx)
    except:
        return None

    
    try:
        coords_y = float(coordy)
    except:
        return None
    
    return Vec(coords_x, coords_y)

def testare_raza(test_raza):
    try:
        raza = float(test_raza)
    except:
        return None
    
    return raza



def main(cercuri):
    area = Vec(100,100)

    raza_min_max = Vec(0,20)

    lista_cercuri_coliziuni = []
    lista_finala = []

    if not isinstance(cercuri, list):
        return None
    
    for testcerc in cercuri:
        if not isinstance(testcerc, list):
            lista_finala.append("Invalid")
            continue
        
        coords = testare_coordonate(testcerc[0], testcerc[1])

        if coords is None:
            lista_finala.append("Invalid")
            continue

        if 0 < coords.x < area.x and 0 < coords.y < area.y:
            pass
        else:
            lista_finala.append("Invalid")
            continue

        raza = testare_raza(testcerc[2])

        if raza is None:
            lista_finala.append("Invalid")
            continue

        if raza_min_max.x > raza or raza_min_max.y < raza:
            lista_finala.append("Invalid")
            continue

        cerc_cur = Circle(coords.x, coords.y ,raza)

        lista = []

        for index, cerc in enumerate(lista_cercuri_coliziuni):
            if collision_cc(cerc, cerc_cur):
                lista.append(index + 1)
        
        lista_finala.append(lista)

        lista_cercuri_coliziuni.append(cerc_cur)

    return lista_finala