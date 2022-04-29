class Vec:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def len(self):
        return (self.x * self.x + self.y * self.y)**0.5

    def __sub__(self, other):
        return Vec(self.x - other.x, self.y - other.y)


class Circle:
    def __init__(self, x=1, y=1, r=1):
        self.pos = Vec(x, y)
        self.r = r


def collision_cc(circle1, circle2):
    d = circle1.pos - circle2.pos
    r = circle1.r + circle2.r

    return d.len() <= r
