def clamp(x, left, right):
    return max(min(x, right), left)

class Vec:
    def __init__(self, x = None, y = None):
        self.x = x
        self.y = y

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

class Rect:
    def __init__(self, x = None, y = None, w = None, h = None):
        self.pos = Vec(x, y)
        self.size = Vec(w, h)

class Circle:
    def __init__(self, x = None, y = None, r = None):
        self.pos = Vec(x, y)
        self.r = r

def collision_r_c(rect, circle):
    rect_center = rect.pos + rect.size / 2
    d = circle.pos - rect_center