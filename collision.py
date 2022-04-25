from cmath import sqrt

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

class Rect:
    def __init__(self, x = None, y = None, w = None, h = None):
        self.pos = Vec(x, y)
        self.size = Vec(w, h)

class Circle:
    def __init__(self, x = None, y = None, r = None):
        self.pos = Vec(x, y)
        self.r = r

def collision_r_r(rect1, rect2):
    collision_x = rect1.pos.x + rect1.size.x > rect2.pos.x and rect2.pos.x + rect2.size.x > rect1.pos.x
    collision_y = rect1.pos.y + rect1.size.y > rect2.pos.y and rect2.pos.y + rect2.size.y > rect1.pos.y

    return collision_x and collision_y

def collision_c_c(circle1, circle2):
    d = circle1.pos - circle2.pos
    r = circle1.r - circle2.r
    
    return d.len2() < r**2

def collision_r_c(rect, circle):
    rect_half = rect.size / 2
    rect_center = rect.pos + rect_half
    d = circle.pos - rect_center
    closest = rect_center + Vec(clamp(d.x, -rect_half.x, rect_half.x), clamp(d.y, -rect_half.y, rect_half.y))

    diff = closest - circle.pos

    return diff.len2() < circle.r**2

def collision_c_r(circle, rect):
    return collision_r_c(rect, circle)