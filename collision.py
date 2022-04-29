from vector import Vec, Circle, collision_cc

ERR_OUT_OF_BOUNDS = "Values out of bounds" # pragma: no mutate

COORDS_MIN = 0
COORDS_MAX = 100

R_MIN = 1
R_MAX = 20


def main(x1, y1, r1, x2, y2, r2):

    coords1 = Vec(float(x1), float(y1))
    coords2 = Vec(float(x2), float(y2))
    r1 = float(r1)
    r2 = float(r2)

    if COORDS_MIN <= coords1.x <= COORDS_MAX:
        pass
    else:
        return ERR_OUT_OF_BOUNDS
    
    if COORDS_MIN <= coords1.y <= COORDS_MAX:
        pass
    else:
        return ERR_OUT_OF_BOUNDS

    if COORDS_MIN <= coords2.x <= COORDS_MAX:
        pass
    else:
        return ERR_OUT_OF_BOUNDS

    if COORDS_MIN <= coords2.y <= COORDS_MAX:
        pass
    else:
        return ERR_OUT_OF_BOUNDS

    if not (R_MIN <= r1 <= R_MAX):
        return ERR_OUT_OF_BOUNDS

    if not (R_MIN <= r2 <= R_MAX):
        return ERR_OUT_OF_BOUNDS

    circle1 = Circle(coords1.x, coords1.y, r1)
    circle2 = Circle(coords2.x, coords2.y, r2)

    circles = [circle1, circle2]

    for i, c1 in enumerate(circles):
        for j, c2 in enumerate(circles):
            if i != j and collision_cc(c1, c2):
                return True

    return False
