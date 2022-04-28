from cmath import sqrt
import re
from sre_compile import isstring

ERR_FORMAT = "Formatul este gresit"
ERR_OUT_OF_BOUNDS = "Valoarea este gresita"


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

    def __str__(self) -> str:
        return f"{self.pos.x}, {self.pos.y}, {self.r}"

def collision_cc(circle1, circle2):
    d = circle1.pos - circle2.pos
    r = circle1.r + circle2.r
    
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

def main(x1, y1, r1, x2, y2, r2):
    area_min = 0
    area_max = 100

    raza_min = 1
    raza_max = 20

    lista_cercuri_coliziuni = []
    
    coords_c1 = testare_coordonate(x1, y1)
    coords_c2 = testare_coordonate(x2, y2)


    if coords_c1 is None:
        return ERR_FORMAT

    if coords_c2 is None:
        return ERR_FORMAT

    if area_min <= coords_c1.x <= area_max and area_min <= coords_c1.y <= area_max:
        pass
    else:
        return ERR_OUT_OF_BOUNDS

    if area_min <= coords_c2.x <= area_max and area_min <= coords_c2.y <= area_max:
        pass
    else:
        return ERR_OUT_OF_BOUNDS
        

    raza_c1 = testare_raza(r1)

    raza_c2 = testare_raza(r2)

    if raza_c1 is None:
        return ERR_FORMAT
    
    if raza_c2 is None:
        return ERR_FORMAT

    if not (raza_min <= raza_c1 <= raza_max):
        return ERR_OUT_OF_BOUNDS

    if not (raza_min <= raza_c2 <= raza_max):
        return ERR_OUT_OF_BOUNDS
        

    cerc1 = Circle(coords_c1.x, coords_c1.y ,raza_c1)
    cerc2 = Circle(coords_c2.x, coords_c2.y, raza_c2)

    lista_cercuri_coliziuni.append(cerc1)
    lista_cercuri_coliziuni.append(cerc2)

    for i, cerc_1 in enumerate(lista_cercuri_coliziuni):
        for j, cerc_2 in enumerate(lista_cercuri_coliziuni):
            if i != j and collision_cc(cerc_1, cerc_2):
                return True
    
    return False