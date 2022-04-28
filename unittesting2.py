import unittest
from collision import *

# Input/Output values

EPS = 1e-7

collision_valid_true = {
    "in" : [(0 + EPS, 1, 8, 9, 3, 2),
             (1, 0 + EPS, 8, 9, 3, 2),
             (9, 1, 1 + EPS, 9, 3, 2),
             (1, 1, 8, 0 + EPS, 3, 2),
             (1, 1, 8, 9, 0 + EPS, 2),
             (1, 1, 8, 9, 3, 1 + EPS),
             (100 - EPS, 1, 8, 92, 3, 10),
             (1, 100 - EPS, 8, 9, 93, 10),
             (1, 1, 20 - EPS, 9, 3, 2),
             (95, 1, 8, 100 - EPS, 3, 2),
             (1, 95, 8, 9, 100 - EPS, 2),
             (1, 1, 8, 9, 3, 20 - EPS),
             (1, 1, 8, 1, 1, 8),
             (1, 1, 8, 11, 1, 2)],
    "out" : True
}

collision_valid_false = {
    "in" : [(0 + EPS, 1, 8, 11, 3, 2),
             (1, 0 + EPS, 8, 9, 13, 2),
             (1, 1, 1 + EPS, 9, 3, 2),
             (1, 1, 4, 0 + EPS, 8, 2),
             (1, 1, 8, 12, 0 + EPS, 2),
             (1, 1, 8, 12, 3, 1 + EPS),
             (100 - EPS, 1, 8, 9, 3, 2),
             (1, 100 - EPS, 8, 9, 3, 2),
             (1, 1, 20 - EPS, 9, 33, 2),
             (1, 1, 8, 100 - EPS, 3, 2),
             (1, 1, 8, 9, 100 - EPS, 2),
             (1, 1, 8, 9, 33, 20 - EPS)],
    "out" : False
}

collision_low_x1 = { 
    "in" : (0 - EPS, 0, 0, 0, 0, 0),
    "out" : ERR_OUT_OF_BOUNDS
}

collision_low_y1 = {
    "in" : (0, 0 - EPS, 0, 0, 0, 0),
    "out" : ERR_OUT_OF_BOUNDS
}

collision_low_r1 = { 
    "in" : (0, 0, 0, 0, 0, 1 - EPS),
    "out" : ERR_OUT_OF_BOUNDS
}

collision_low_x2 = {
    "in" : (0, 0, 0, 0 - EPS, 0, 0),
    "out" : ERR_OUT_OF_BOUNDS
}

collision_low_y2 = {
    "in" : (0, 0, 0, 0, 0 - EPS, 0),
    "out" : ERR_OUT_OF_BOUNDS
}

collision_low_r2 = {
    "in" : (0, 0, 1, 0, 0, 1 - EPS),
    "out" : ERR_OUT_OF_BOUNDS
}

collision_high_x1 = {
    "in" : (100 + EPS, 0, 0, 0, 0, 0),
    "out" : ERR_OUT_OF_BOUNDS
}

collision_high_y1 = {
    "in" : (0, 100 + EPS, 0, 0, 0, 0),
    "out" : ERR_OUT_OF_BOUNDS
}

collision_high_r1 = {
    "in" : (0, 0, 20 + EPS, 0, 0, 0),
    "out" : ERR_OUT_OF_BOUNDS
}
collision_high_x2 = {
    "in" : (0, 0, 0, 100 + EPS, 0, 0),
    "out" : ERR_OUT_OF_BOUNDS
}

collision_high_y2 = {
    "in" : (0, 0, 0, 0, 100 + EPS, 0),
    "out" : ERR_OUT_OF_BOUNDS
}

collision_high_r2 = {
    "in" : (0, 0, 1, 0, 0, 20 + EPS),
    "out" : ERR_OUT_OF_BOUNDS
}

class TestCollision(unittest.TestCase):

# -------------------- VALID ARGS -----------------------------------

    def test_collision_valid_true0(self):
        x1, y1, r1, x2, y2, r2 = collision_valid_true["in"][0]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_valid_true["out"])
    
    def test_collision_valid_true1(self):
        x1, y1, r1, x2, y2, r2 = collision_valid_true["in"][1]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_valid_true["out"])
    
    def test_collision_valid_true2(self):
        x1, y1, r1, x2, y2, r2 = collision_valid_true["in"][2]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_valid_true["out"])
    
    def test_collision_valid_true3(self):
        x1, y1, r1, x2, y2, r2 = collision_valid_true["in"][3]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_valid_true["out"])
    
    def test_collision_valid_true4(self):
        x1, y1, r1, x2, y2, r2 = collision_valid_true["in"][4]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_valid_true["out"])
    
    def test_collision_valid_true5(self):
        x1, y1, r1, x2, y2, r2 = collision_valid_true["in"][5]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_valid_true["out"])
    
    def test_collision_valid_true6(self):
        x1, y1, r1, x2, y2, r2 = collision_valid_true["in"][6]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_valid_true["out"])
    
    def test_collision_valid_true7(self):
        x1, y1, r1, x2, y2, r2 = collision_valid_true["in"][7]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_valid_true["out"])
    
    def test_collision_valid_true8(self):
        x1, y1, r1, x2, y2, r2 = collision_valid_true["in"][8]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_valid_true["out"])
    
    def test_collision_valid_true9(self):
        x1, y1, r1, x2, y2, r2 = collision_valid_true["in"][9]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_valid_true["out"])
    
    def test_collision_valid_true10(self):
        x1, y1, r1, x2, y2, r2 = collision_valid_true["in"][10]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_valid_true["out"])
    
    def test_collision_valid_true11(self):
        x1, y1, r1, x2, y2, r2 = collision_valid_true["in"][11]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_valid_true["out"])

    def test_collision_valid_true12(self):
        x1, y1, r1, x2, y2, r2 = collision_valid_true["in"][12]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_valid_true["out"])

    def test_collision_valid_true13(self):
        x1, y1, r1, x2, y2, r2 = collision_valid_true["in"][13]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_valid_true["out"])
    
    def test_collision_valid_false0(self):
        x1, y1, r1, x2, y2, r2 = collision_valid_false["in"][0]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_valid_false["out"])

    def test_collision_valid_false1(self):
        x1, y1, r1, x2, y2, r2 = collision_valid_false["in"][1]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_valid_false["out"])

    def test_collision_valid_false2(self):
        x1, y1, r1, x2, y2, r2 = collision_valid_false["in"][2]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_valid_false["out"])

    def test_collision_valid_false3(self):
        x1, y1, r1, x2, y2, r2 = collision_valid_false["in"][3]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_valid_false["out"])

    def test_collision_valid_false4(self):
        x1, y1, r1, x2, y2, r2 = collision_valid_false["in"][4]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_valid_false["out"])

    def test_collision_valid_false5(self):
        x1, y1, r1, x2, y2, r2 = collision_valid_false["in"][5]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_valid_false["out"])

    def test_collision_valid_false6(self):
        x1, y1, r1, x2, y2, r2 = collision_valid_false["in"][6]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_valid_false["out"])

    def test_collision_valid_false7(self):
        x1, y1, r1, x2, y2, r2 = collision_valid_false["in"][7]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_valid_false["out"])

    def test_collision_valid_false8(self):
        x1, y1, r1, x2, y2, r2 = collision_valid_false["in"][8]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_valid_false["out"])

    def test_collision_valid_false9(self):
        x1, y1, r1, x2, y2, r2 = collision_valid_false["in"][9]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_valid_false["out"])

    def test_collision_valid_false10(self):
        x1, y1, r1, x2, y2, r2 = collision_valid_false["in"][10]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_valid_false["out"])

    def test_collision_valid_false11(self):
        x1, y1, r1, x2, y2, r2 = collision_valid_false["in"][11]
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

if __name__ == '__main__':
    unittest.main()