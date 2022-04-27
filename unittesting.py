import unittest
from collision import *

lista_cercuri_test_1 = [[1,1,5], [-1,1,1], ['asd',1,23], [1,1,'ad'], [1,1,3]]
rezultat1 = [[], "Invalid", "Invalid", "Invalid", [1]]

class TestCollision(unittest.TestCase):
    def test1(self):
        result = main(lista_cercuri_test_1)
        self.assertEqual(result,rezultat1)

unittest.main()