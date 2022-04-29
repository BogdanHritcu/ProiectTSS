import unittest
from collision import *

# Input/Output values

collision_valid_true = {
    "in": (1, 1, 8, 9, 3, 2),
    "out": True
}

collision_valid_false = {
    "in": (30, 30, 2, 7, 8, 3),
    "out": False
}

collision_low_x1 = {
    "in": (-2, 0, 0, 0, 0, 0),
    "out": ERR_OUT_OF_BOUNDS
}

collision_low_y1 = {
    "in": (0, -2, 0, 0, 0, 0),
    "out": ERR_OUT_OF_BOUNDS
}

collision_low_r1 = {
    "in": (0, 0, 0, 0, 0, 0),
    "out": ERR_OUT_OF_BOUNDS
}

collision_low_x2 = {
    "in": (0, 0, 0, -2, 0, 0),
    "out": ERR_OUT_OF_BOUNDS
}

collision_low_y2 = {
    "in": (0, 0, 0, 0, -2, 0),
    "out": ERR_OUT_OF_BOUNDS
}

collision_low_r2 = {
    "in": (0, 0, 0, 0, 1, 0),
    "out": ERR_OUT_OF_BOUNDS
}

collision_high_x1 = {
    "in": (101, 0, 0, 0, 0, 0),
    "out": ERR_OUT_OF_BOUNDS
}

collision_high_y1 = {
    "in": (0, 101, 0, 0, 0, 0),
    "out": ERR_OUT_OF_BOUNDS
}

collision_high_r1 = {
    "in": (0, 0, 21, 0, 0, 0),
    "out": ERR_OUT_OF_BOUNDS
}
collision_high_x2 = {
    "in": (0, 0, 0, 101, 0, 0),
    "out": ERR_OUT_OF_BOUNDS
}

collision_high_y2 = {
    "in": (0, 0, 0, 0, 101, 0),
    "out": ERR_OUT_OF_BOUNDS
}

collision_high_r2 = {
    "in": (0, 0, 1, 0, 0, 21),
    "out": ERR_OUT_OF_BOUNDS
}

mutant_1 = {
    "in": (0, 0, 2, 90, 90, 2),
    "out": False
}

mutant_2 = {
    "in": (0, 0, 2, 101, 101, 2),
    "out": ERR_OUT_OF_BOUNDS
}

mutant_3 = {
    "in": (0, 0, 1, 100, 100, 2),
    "out": False
}

mutant_4 = {
    "in": (100, 100, 1, 0, 0, 2),
    "out": False
}

mutant_5 = {
    "in": (100, 100, 20, 0, 0, 20),
    "out": False
}

mutant_6 = {
    "in": (100, 100, 10, 0, 0, 1),
    "out": False
}

mutant_7 = {
    "in": (100, 100, 10, 0, 0, 20),
    "out": False
}

class TestCollision(unittest.TestCase):

    # -------------------- VALID ARGS -----------------------------------

    def test_collision_valid_true(self):
        x1, y1, r1, x2, y2, r2 = collision_valid_true["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_valid_true["out"])

    def test_collision_valid_false(self):
        x1, y1, r1, x2, y2, r2 = collision_valid_false["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_valid_false["out"])

# -------------------- LOWER VALUES --------------------------------

    def test_collision_low_x1(self):
        x1, y1, r1, x2, y2, r2 = collision_low_x1["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_low_x1["out"])

    def test_collision_low_y1(self):
        x1, y1, r1, x2, y2, r2 = collision_low_y1["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_low_y1["out"])

    def test_collision_low_r1(self):
        x1, y1, r1, x2, y2, r2 = collision_low_r1["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_low_r1["out"])

    def test_collision_low_x2(self):
        x1, y1, r1, x2, y2, r2 = collision_low_x2["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_low_x2["out"])

    def test_collision_low_y2(self):
        x1, y1, r1, x2, y2, r2 = collision_low_y2["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_low_y1["out"])

    def test_collision_low_r2(self):
        x1, y1, r1, x2, y2, r2 = collision_low_r2["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_low_r2["out"])

# -------------------- HIGHER VALUES ----------------------------

    def test_collision_high_x1(self):
        x1, y1, r1, x2, y2, r2 = collision_high_x1["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_high_x1["out"])

    def test_collision_high_y1(self):
        x1, y1, r1, x2, y2, r2 = collision_high_y1["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_high_y1["out"])

    def test_collision_high_r1(self):
        x1, y1, r1, x2, y2, r2 = collision_high_r1["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_high_r1["out"])

    def test_collision_high_x2(self):
        x1, y1, r1, x2, y2, r2 = collision_high_x2["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_high_x2["out"])

    def test_collision_high_y2(self):
        x1, y1, r1, x2, y2, r2 = collision_high_y2["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_high_y1["out"])

    def test_collision_high_r2(self):
        x1, y1, r1, x2, y2, r2 = collision_high_r2["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_high_r2["out"])

    def test_mutant1(self):
        x1, y1, r1, x2, y2, r2 = mutant_1["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, mutant_1["out"])

    def test_mutant2(self):
        x1, y1, r1, x2, y2, r2 = mutant_2["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, mutant_2["out"])

    def test_mutant3(self):
        x1, y1, r1, x2, y2, r2 = mutant_3["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, mutant_3["out"])

    def test_mutant4(self):
        x1, y1, r1, x2, y2, r2 = mutant_4["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, mutant_4["out"])

    def test_mutant5(self):
        x1, y1, r1, x2, y2, r2 = mutant_5["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, mutant_5["out"])

    def test_mutant6(self):
        x1, y1, r1, x2, y2, r2 = mutant_6["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, mutant_6["out"])

    def test_mutant7(self):
        x1, y1, r1, x2, y2, r2 = mutant_7["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, mutant_7["out"])

if __name__ == '__main__':
    unittest.main()
