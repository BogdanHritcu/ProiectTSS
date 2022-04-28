import unittest
from collision import *

# lista intrare

lista_coliziune_true = (1, 1, 8, 9, 3, 2)
lista_coliziune_false = (0, 3, 2, 7, 8, 3)

lista_coordonate_x1_cifre_mici =(-2, 0, 0, 0, 0, 0)
lista_coordonate_y1_cifre_mici =(0, -2, 0, 0, 0, 0)
lista_raza1_cifre_mici =(0, 0, 0, 0, 0, 0)
lista_coordonate_x2_cifre_mici =(0, 0, 0, -2, 0, 0)
lista_coordonate_y2_cifre_mici =(0, 0, 0, 0, -2, 0)
lista_raza2_cifre_mici =(0, 0, 0, 0, 0, 0)

lista_coordonate_x1_cifre_mari =(101, 0, 0, 0, 0, 0)
lista_coordonate_y1_cifre_mari =(0, 101, 0, 0, 0, 0)
lista_raza1_cifre_mari =(0, 0, 21, 0, 0, 0)
lista_coordonate_x2_cifre_mari =(0, 0, 0, 101, 0, 0)
lista_coordonate_y2_cifre_mari =(0, 0, 0, 0, 101, 0)
lista_raza2_cifre_mari =(0, 0, 0, 0, 0, 21)

# lista rezultate

rezultat_coliziune_true = True
rezultat_coliziune_false = False

rezultat_coordonate_x1_cifre_mici = ERR_OUT_OF_BOUNDS
rezultat_coordonate_x1_cifre_mari = ERR_OUT_OF_BOUNDS

rezultat_coordonate_y1_cifre_mici = ERR_OUT_OF_BOUNDS
rezultat_coordonate_y1_cifre_mari = ERR_OUT_OF_BOUNDS

rezultat_raza1_cifre_mici = ERR_OUT_OF_BOUNDS
rezultat_raza1_cifre_mari = ERR_OUT_OF_BOUNDS

rezultat_coordonate_x2_cifre_mici = ERR_OUT_OF_BOUNDS
rezultat_coordonate_x2_cifre_mari = ERR_OUT_OF_BOUNDS

rezultat_coordonate_y2_cifre_mici = ERR_OUT_OF_BOUNDS
rezultat_coordonate_y2_cifre_mari = ERR_OUT_OF_BOUNDS

rezultat_raza2_cifre_mici = ERR_OUT_OF_BOUNDS
rezultat_raza2_cifre_mari = ERR_OUT_OF_BOUNDS


class TestCollision(unittest.TestCase):

# -------------------- COLIZIUNE -----------------------------------

    def test_coliziune_true(self):
        x1, y1, r1, x2, y2, r2 = lista_coliziune_true
        rezultat = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(rezultat, rezultat_coliziune_true)

    def test_coliziune_false(self):
        x1, y1, r1, x2, y2, r2 = lista_coliziune_false
        rezultat = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(rezultat, rezultat_coliziune_false)
    
# -------------------- COORDONATE X CERC 1 -------------------------

    def test_coordonate_x1_cifre_mici(self):
        x1, y1, r1, x2, y2, r2 = lista_coordonate_x1_cifre_mici
        rezultat = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(rezultat, rezultat_coordonate_x1_cifre_mici)

    def test_coordonate_x1_cifre_mari(self):
        x1, y1, r1, x2, y2, r2 = lista_coordonate_x1_cifre_mari
        rezultat = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(rezultat, rezultat_coordonate_x1_cifre_mari)

# -------------------- COORDONATE Y CERC 1 -------------------------

    def test_coordonate_y1_cifre_mici(self):
        x1, y1, r1, x2, y2, r2 = lista_coordonate_y1_cifre_mici
        rezultat = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(rezultat, rezultat_coordonate_y1_cifre_mici)

    def test_coordonate_y1_cifre_mari(self):
        x1, y1, r1, x2, y2, r2 = lista_coordonate_y1_cifre_mari
        rezultat = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(rezultat, rezultat_coordonate_y1_cifre_mari)

# -------------------- COORDONATE X CERC 2 -------------------------

    def test_coordonate_x2_cifre_mici(self):
        x1, y1, r1, x2, y2, r2 = lista_coordonate_x2_cifre_mici
        rezultat = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(rezultat, rezultat_coordonate_x2_cifre_mici)
    
    def test_coordonate_x2_cifre_mari(self):
        x1, y1, r1, x2, y2, r2 = lista_coordonate_x2_cifre_mari
        rezultat = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(rezultat, rezultat_coordonate_x2_cifre_mari)

# -------------------- COORDONATE Y CERC 2 -------------------------

    def test_coordonate_y2_cifre_mici(self):
        x1, y1, r1, x2, y2, r2 = lista_coordonate_y2_cifre_mici
        rezultat = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(rezultat, rezultat_coordonate_y2_cifre_mici)

    def test_coordonate_y2_cifre_mari(self):
        x1, y1, r1, x2, y2, r2 = lista_coordonate_y2_cifre_mari
        rezultat = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(rezultat, rezultat_coordonate_y2_cifre_mari)

# -------------------- RAZA CERC 1 ---------------------------------

    def test_raza_cifre_mici(self):
        x1, y1, r1, x2, y2, r2 = lista_raza1_cifre_mici
        rezultat = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(rezultat, rezultat_raza1_cifre_mici)
    
    def test_raza_cifre_mari(self):
        x1, y1, r1, x2, y2, r2 = lista_raza1_cifre_mari
        rezultat = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(rezultat, rezultat_raza1_cifre_mari)
        
# -------------------- RAZA CERC 2 ---------------------------------

    def test_raza_cifre_mici(self):
        x1, y1, r1, x2, y2, r2 = lista_raza2_cifre_mici
        rezultat = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(rezultat, rezultat_raza2_cifre_mici)
    
    def test_raza_cifre_mari(self):
        x1, y1, r1, x2, y2, r2 = lista_raza2_cifre_mari
        rezultat = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(rezultat, rezultat_raza2_cifre_mari)

unittest.main()

