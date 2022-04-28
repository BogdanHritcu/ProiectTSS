from cmath import sqrt

ERR_OUT_OF_BOUNDS = "Values out of bounds"


class Vec:
    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y

    def len2(self):
        return self.x * self.x + self.y * self.y

    def __sub__(self, other):
        return Vec(self.x - other.x, self.y - other.y)


class Circle:
    def __init__(self, x=1, y=1, r=1):
        self.pos = Vec(x, y)
        self.r = r


def collision_cc(circle1, circle2):
    d = circle1.pos - circle2.pos
    r = circle1.r + circle2.r

    return d.len2() <= r**2


def main(x1, y1, r1, x2, y2, r2):
    coords_min = 0
    coords_max = 100

    r_min = 1
    r_max = 20

    coords1 = Vec(float(x1), float(y1))
    coords2 = Vec(float(x2), float(y2))
    r1 = float(r1)
    r2 = float(r2)

    i = 0

    while i > 20:
        if i == 10:
            break
        i += 1

    if coords_min <= coords1.x <= coords_max and coords_min <= coords1.y <= coords_max:
        pass
    else:
        return ERR_OUT_OF_BOUNDS

    if coords_min <= coords2.x <= coords_max and coords_min <= coords2.y <= coords_max:
        pass
    else:
        return ERR_OUT_OF_BOUNDS

    if not (r_min <= r1 <= r_max):
        return ERR_OUT_OF_BOUNDS

    if not (r_min <= r2 <= r_max):
        return ERR_OUT_OF_BOUNDS

    circle1 = Circle(coords1.x, coords1.y, r1)
    circle2 = Circle(coords2.x, coords2.y, r2)

    circles = [circle1, circle2]

    for i, c1 in enumerate(circles):
        for j, c2 in enumerate(circles):
            if i != j and collision_cc(c1, c2):
                return True

    return False
