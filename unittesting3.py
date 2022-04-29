import unittest
from collision import *

# Input/Output values

collision_x1_1 = {
    "in" : (-3.723, 58.602, 10.128, 89.114, 2.529, 5.459),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_2 = {
    "in" : (-1e-07, 74.894, 17.171, 31.125, 66.148, 15.653),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_1 = {
    "in" : (0, -2.586, 10.577, 78.241, 70.509, 18.299),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_2 = {
    "in" : (0, -1e-07, 3.062, 5.336, 18.551, 19.319),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_3r1_1 = {
    "in" : (0, 0, -2.427, 86.615, 73.89, 15.694),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_3r1_2 = {
    "in" : (0, 0, 0.9999999, 11.61, 57.575, 6.17),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_3r1_3x2_1 = {
    "in" : (0, 0, 1, -3.536, 26.527, 6.246),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_3r1_3x2_2 = {
    "in" : (0, 0, 1, -1e-07, 31.609, 7.803),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_3r1_3x2_3y2_1 = {
    "in" : (0, 0, 1, 0, -2.726, 11.417),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_3r1_3x2_3y2_2 = {
    "in" : (0, 0, 1, 0, -1e-07, 8.922),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_3r1_3x2_3y2_3r2_1 = {
    "in" : (0, 0, 1, 0, 0, -2.261),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_3r1_3x2_3y2_3r2_2 = {
    "in" : (0, 0, 1, 0, 0, 0.9999999),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_3r1_3x2_3y2_3r2_3 = {
    "in" : (0, 0, 1, 0, 0, 1),
    "out" : True
}
        
collision_x1_3y1_3r1_3x2_3y2_3r2_5 = {
    "in" : (0, 0, 1, 0, 0, 20),
    "out" : True
}
        
collision_x1_3y1_3r1_3x2_3y2_3r2_6 = {
    "in" : (0, 0, 1, 0, 0, 20.0000001),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_3r1_3x2_3y2_3r2_7 = {
    "in" : (0, 0, 1, 0, 0, 23.255),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_3r1_3x2_3y2_5r2_1 = {
    "in" : (0, 0, 1, 0, 100, -2.473),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_3r1_3x2_3y2_5r2_2 = {
    "in" : (0, 0, 1, 0, 100, 0.9999999),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_3r1_3x2_3y2_5r2_3 = {
    "in" : (0, 0, 1, 0, 100, 1),
    "out" : False
}
        
collision_x1_3y1_3r1_3x2_3y2_5r2_5 = {
    "in" : (0, 0, 1, 0, 100, 20),
    "out" : False
}
        
collision_x1_3y1_3r1_3x2_3y2_5r2_6 = {
    "in" : (0, 0, 1, 0, 100, 20.0000001),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_3r1_3x2_3y2_5r2_7 = {
    "in" : (0, 0, 1, 0, 100, 22.958),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_3r1_3x2_3y2_6 = {
    "in" : (0, 0, 1, 0, 100.0000001, 18.269),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_3r1_3x2_3y2_7 = {
    "in" : (0, 0, 1, 0, 102.416, 8.107),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_3r1_3x2_5y2_1 = {
    "in" : (0, 0, 1, 100, -2.752, 10.137),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_3r1_3x2_5y2_2 = {
    "in" : (0, 0, 1, 100, -1e-07, 19.66),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_3r1_3x2_5y2_3r2_1 = {
    "in" : (0, 0, 1, 100, 0, -1.978),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_3r1_3x2_5y2_3r2_2 = {
    "in" : (0, 0, 1, 100, 0, 0.9999999),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_3r1_3x2_5y2_3r2_3 = {
    "in" : (0, 0, 1, 100, 0, 1),
    "out" : False
}
        
collision_x1_3y1_3r1_3x2_5y2_3r2_5 = {
    "in" : (0, 0, 1, 100, 0, 20),
    "out" : False
}
        
collision_x1_3y1_3r1_3x2_5y2_3r2_6 = {
    "in" : (0, 0, 1, 100, 0, 20.0000001),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_3r1_3x2_5y2_3r2_7 = {
    "in" : (0, 0, 1, 100, 0, 22.698),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_3r1_3x2_5y2_5r2_1 = {
    "in" : (0, 0, 1, 100, 100, -1.352),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_3r1_3x2_5y2_5r2_2 = {
    "in" : (0, 0, 1, 100, 100, 0.9999999),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_3r1_3x2_5y2_5r2_3 = {
    "in" : (0, 0, 1, 100, 100, 1),
    "out" : False
}
        
collision_x1_3y1_3r1_3x2_5y2_5r2_5 = {
    "in" : (0, 0, 1, 100, 100, 20),
    "out" : False
}
        
collision_x1_3y1_3r1_3x2_5y2_5r2_6 = {
    "in" : (0, 0, 1, 100, 100, 20.0000001),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_3r1_3x2_5y2_5r2_7 = {
    "in" : (0, 0, 1, 100, 100, 22.979),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_3r1_3x2_5y2_6 = {
    "in" : (0, 0, 1, 100, 100.0000001, 15.277),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_3r1_3x2_5y2_7 = {
    "in" : (0, 0, 1, 100, 103.86, 9.825),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_3r1_3x2_6 = {
    "in" : (0, 0, 1, 100.0000001, 31.886, 11.879),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_3r1_3x2_7 = {
    "in" : (0, 0, 1, 102.852, 55.504, 9.415),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_3r1_5x2_1 = {
    "in" : (0, 0, 20, -3.228, 64.577, 10.529),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_3r1_5x2_2 = {
    "in" : (0, 0, 20, -1e-07, 6.114, 7.365),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_3r1_5x2_3y2_1 = {
    "in" : (0, 0, 20, 0, -3.9, 5.099),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_3r1_5x2_3y2_2 = {
    "in" : (0, 0, 20, 0, -1e-07, 19.605),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_3r1_5x2_3y2_3r2_1 = {
    "in" : (0, 0, 20, 0, 0, -1.617),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_3r1_5x2_3y2_3r2_2 = {
    "in" : (0, 0, 20, 0, 0, 0.9999999),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_3r1_5x2_3y2_3r2_3 = {
    "in" : (0, 0, 20, 0, 0, 1),
    "out" : True
}
        
collision_x1_3y1_3r1_5x2_3y2_3r2_5 = {
    "in" : (0, 0, 20, 0, 0, 20),
    "out" : True
}
        
collision_x1_3y1_3r1_5x2_3y2_3r2_6 = {
    "in" : (0, 0, 20, 0, 0, 20.0000001),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_3r1_5x2_3y2_3r2_7 = {
    "in" : (0, 0, 20, 0, 0, 23.411),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_3r1_5x2_3y2_5r2_1 = {
    "in" : (0, 0, 20, 0, 100, -2.163),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_3r1_5x2_3y2_5r2_2 = {
    "in" : (0, 0, 20, 0, 100, 0.9999999),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_3r1_5x2_3y2_5r2_3 = {
    "in" : (0, 0, 20, 0, 100, 1),
    "out" : False
}
        
collision_x1_3y1_3r1_5x2_3y2_5r2_5 = {
    "in" : (0, 0, 20, 0, 100, 20),
    "out" : False
}
        
collision_x1_3y1_3r1_5x2_3y2_5r2_6 = {
    "in" : (0, 0, 20, 0, 100, 20.0000001),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_3r1_5x2_3y2_5r2_7 = {
    "in" : (0, 0, 20, 0, 100, 23.465),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_3r1_5x2_3y2_6 = {
    "in" : (0, 0, 20, 0, 100.0000001, 1.045),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_3r1_5x2_3y2_7 = {
    "in" : (0, 0, 20, 0, 102.612, 11.638),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_3r1_5x2_5y2_1 = {
    "in" : (0, 0, 20, 100, -2.513, 13.256),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_3r1_5x2_5y2_2 = {
    "in" : (0, 0, 20, 100, -1e-07, 10.653),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_3r1_5x2_5y2_3r2_1 = {
    "in" : (0, 0, 20, 100, 0, -1.545),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_3r1_5x2_5y2_3r2_2 = {
    "in" : (0, 0, 20, 100, 0, 0.9999999),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_3r1_5x2_5y2_3r2_3 = {
    "in" : (0, 0, 20, 100, 0, 1),
    "out" : False
}
        
collision_x1_3y1_3r1_5x2_5y2_3r2_5 = {
    "in" : (0, 0, 20, 100, 0, 20),
    "out" : False
}
        
collision_x1_3y1_3r1_5x2_5y2_3r2_6 = {
    "in" : (0, 0, 20, 100, 0, 20.0000001),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_3r1_5x2_5y2_3r2_7 = {
    "in" : (0, 0, 20, 100, 0, 22.087),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_3r1_5x2_5y2_5r2_1 = {
    "in" : (0, 0, 20, 100, 100, -2.729),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_3r1_5x2_5y2_5r2_2 = {
    "in" : (0, 0, 20, 100, 100, 0.9999999),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_3r1_5x2_5y2_5r2_3 = {
    "in" : (0, 0, 20, 100, 100, 1),
    "out" : False
}
        
collision_x1_3y1_3r1_5x2_5y2_5r2_5 = {
    "in" : (0, 0, 20, 100, 100, 20),
    "out" : False
}
        
collision_x1_3y1_3r1_5x2_5y2_5r2_6 = {
    "in" : (0, 0, 20, 100, 100, 20.0000001),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_3r1_5x2_5y2_5r2_7 = {
    "in" : (0, 0, 20, 100, 100, 23.519),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_3r1_5x2_5y2_6 = {
    "in" : (0, 0, 20, 100, 100.0000001, 11.248),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_3r1_5x2_5y2_7 = {
    "in" : (0, 0, 20, 100, 102.092, 1.112),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_3r1_5x2_6 = {
    "in" : (0, 0, 20, 100.0000001, 46.927, 7.261),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_3r1_5x2_7 = {
    "in" : (0, 0, 20, 103.439, 89.538, 17.86),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_3r1_6 = {
    "in" : (0, 0, 20.0000001, 15.192, 14.237, 7.95),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_3r1_7 = {
    "in" : (0, 0, 22.973, 83.584, 20.283, 10.397),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_5r1_1 = {
    "in" : (0, 100, -2.979, 47.798, 88.302, 19.545),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_5r1_2 = {
    "in" : (0, 100, 0.9999999, 85.201, 77.497, 4.432),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_5r1_3x2_1 = {
    "in" : (0, 100, 1, -3.683, 30.165, 12.945),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_5r1_3x2_2 = {
    "in" : (0, 100, 1, -1e-07, 57.666, 2.026),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_5r1_3x2_3y2_1 = {
    "in" : (0, 100, 1, 0, -2.406, 13.168),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_5r1_3x2_3y2_2 = {
    "in" : (0, 100, 1, 0, -1e-07, 6.429),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_5r1_3x2_3y2_3r2_1 = {
    "in" : (0, 100, 1, 0, 0, -2.871),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_5r1_3x2_3y2_3r2_2 = {
    "in" : (0, 100, 1, 0, 0, 0.9999999),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_5r1_3x2_3y2_3r2_3 = {
    "in" : (0, 100, 1, 0, 0, 1),
    "out" : False
}
        
collision_x1_3y1_5r1_3x2_3y2_3r2_5 = {
    "in" : (0, 100, 1, 0, 0, 20),
    "out" : False
}
        
collision_x1_3y1_5r1_3x2_3y2_3r2_6 = {
    "in" : (0, 100, 1, 0, 0, 20.0000001),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_5r1_3x2_3y2_3r2_7 = {
    "in" : (0, 100, 1, 0, 0, 22.928),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_5r1_3x2_3y2_5r2_1 = {
    "in" : (0, 100, 1, 0, 100, -1.314),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_5r1_3x2_3y2_5r2_2 = {
    "in" : (0, 100, 1, 0, 100, 0.9999999),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_5r1_3x2_3y2_5r2_3 = {
    "in" : (0, 100, 1, 0, 100, 1),
    "out" : True
}
        
collision_x1_3y1_5r1_3x2_3y2_5r2_5 = {
    "in" : (0, 100, 1, 0, 100, 20),
    "out" : True
}
        
collision_x1_3y1_5r1_3x2_3y2_5r2_6 = {
    "in" : (0, 100, 1, 0, 100, 20.0000001),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_5r1_3x2_3y2_5r2_7 = {
    "in" : (0, 100, 1, 0, 100, 22.276),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_5r1_3x2_3y2_6 = {
    "in" : (0, 100, 1, 0, 100.0000001, 9.289),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_5r1_3x2_3y2_7 = {
    "in" : (0, 100, 1, 0, 103.679, 17.168),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_5r1_3x2_5y2_1 = {
    "in" : (0, 100, 1, 100, -3.849, 3.157),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_5r1_3x2_5y2_2 = {
    "in" : (0, 100, 1, 100, -1e-07, 13.644),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_5r1_3x2_5y2_3r2_1 = {
    "in" : (0, 100, 1, 100, 0, -2.995),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_5r1_3x2_5y2_3r2_2 = {
    "in" : (0, 100, 1, 100, 0, 0.9999999),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_5r1_3x2_5y2_3r2_3 = {
    "in" : (0, 100, 1, 100, 0, 1),
    "out" : False
}
        
collision_x1_3y1_5r1_3x2_5y2_3r2_5 = {
    "in" : (0, 100, 1, 100, 0, 20),
    "out" : False
}
        
collision_x1_3y1_5r1_3x2_5y2_3r2_6 = {
    "in" : (0, 100, 1, 100, 0, 20.0000001),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_5r1_3x2_5y2_3r2_7 = {
    "in" : (0, 100, 1, 100, 0, 22.486),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_5r1_3x2_5y2_5r2_1 = {
    "in" : (0, 100, 1, 100, 100, -1.913),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_5r1_3x2_5y2_5r2_2 = {
    "in" : (0, 100, 1, 100, 100, 0.9999999),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_5r1_3x2_5y2_5r2_3 = {
    "in" : (0, 100, 1, 100, 100, 1),
    "out" : False
}
        
collision_x1_3y1_5r1_3x2_5y2_5r2_5 = {
    "in" : (0, 100, 1, 100, 100, 20),
    "out" : False
}
        
collision_x1_3y1_5r1_3x2_5y2_5r2_6 = {
    "in" : (0, 100, 1, 100, 100, 20.0000001),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_5r1_3x2_5y2_5r2_7 = {
    "in" : (0, 100, 1, 100, 100, 22.422),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_5r1_3x2_5y2_6 = {
    "in" : (0, 100, 1, 100, 100.0000001, 13.374),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_5r1_3x2_5y2_7 = {
    "in" : (0, 100, 1, 100, 102.73, 4.499),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_5r1_3x2_6 = {
    "in" : (0, 100, 1, 100.0000001, 31.078, 16.02),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_5r1_3x2_7 = {
    "in" : (0, 100, 1, 102.064, 79.767, 9.595),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_5r1_5x2_1 = {
    "in" : (0, 100, 20, -2.93, 31.384, 12.057),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_5r1_5x2_2 = {
    "in" : (0, 100, 20, -1e-07, 5.663, 18.356),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_5r1_5x2_3y2_1 = {
    "in" : (0, 100, 20, 0, -2.498, 11.693),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_5r1_5x2_3y2_2 = {
    "in" : (0, 100, 20, 0, -1e-07, 11.782),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_5r1_5x2_3y2_3r2_1 = {
    "in" : (0, 100, 20, 0, 0, -2.975),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_5r1_5x2_3y2_3r2_2 = {
    "in" : (0, 100, 20, 0, 0, 0.9999999),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_5r1_5x2_3y2_3r2_3 = {
    "in" : (0, 100, 20, 0, 0, 1),
    "out" : False
}
        
collision_x1_3y1_5r1_5x2_3y2_3r2_5 = {
    "in" : (0, 100, 20, 0, 0, 20),
    "out" : False
}
        
collision_x1_3y1_5r1_5x2_3y2_3r2_6 = {
    "in" : (0, 100, 20, 0, 0, 20.0000001),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_5r1_5x2_3y2_3r2_7 = {
    "in" : (0, 100, 20, 0, 0, 22.187),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_5r1_5x2_3y2_5r2_1 = {
    "in" : (0, 100, 20, 0, 100, -2.001),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_5r1_5x2_3y2_5r2_2 = {
    "in" : (0, 100, 20, 0, 100, 0.9999999),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_5r1_5x2_3y2_5r2_3 = {
    "in" : (0, 100, 20, 0, 100, 1),
    "out" : True
}
        
collision_x1_3y1_5r1_5x2_3y2_5r2_5 = {
    "in" : (0, 100, 20, 0, 100, 20),
    "out" : True
}
        
collision_x1_3y1_5r1_5x2_3y2_5r2_6 = {
    "in" : (0, 100, 20, 0, 100, 20.0000001),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_5r1_5x2_3y2_5r2_7 = {
    "in" : (0, 100, 20, 0, 100, 23.109),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_5r1_5x2_3y2_6 = {
    "in" : (0, 100, 20, 0, 100.0000001, 16.857),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_5r1_5x2_3y2_7 = {
    "in" : (0, 100, 20, 0, 102.801, 7.185),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_5r1_5x2_5y2_1 = {
    "in" : (0, 100, 20, 100, -2.837, 8.044),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_5r1_5x2_5y2_2 = {
    "in" : (0, 100, 20, 100, -1e-07, 2.408),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_5r1_5x2_5y2_3r2_1 = {
    "in" : (0, 100, 20, 100, 0, -1.703),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_5r1_5x2_5y2_3r2_2 = {
    "in" : (0, 100, 20, 100, 0, 0.9999999),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_5r1_5x2_5y2_3r2_3 = {
    "in" : (0, 100, 20, 100, 0, 1),
    "out" : False
}
        
collision_x1_3y1_5r1_5x2_5y2_3r2_5 = {
    "in" : (0, 100, 20, 100, 0, 20),
    "out" : False
}
        
collision_x1_3y1_5r1_5x2_5y2_3r2_6 = {
    "in" : (0, 100, 20, 100, 0, 20.0000001),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_5r1_5x2_5y2_3r2_7 = {
    "in" : (0, 100, 20, 100, 0, 23.842),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_5r1_5x2_5y2_5r2_1 = {
    "in" : (0, 100, 20, 100, 100, -2.219),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_5r1_5x2_5y2_5r2_2 = {
    "in" : (0, 100, 20, 100, 100, 0.9999999),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_5r1_5x2_5y2_5r2_3 = {
    "in" : (0, 100, 20, 100, 100, 1),
    "out" : False
}
        
collision_x1_3y1_5r1_5x2_5y2_5r2_5 = {
    "in" : (0, 100, 20, 100, 100, 20),
    "out" : False
}
        
collision_x1_3y1_5r1_5x2_5y2_5r2_6 = {
    "in" : (0, 100, 20, 100, 100, 20.0000001),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_5r1_5x2_5y2_5r2_7 = {
    "in" : (0, 100, 20, 100, 100, 22.146),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_5r1_5x2_5y2_6 = {
    "in" : (0, 100, 20, 100, 100.0000001, 17.399),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_5r1_5x2_5y2_7 = {
    "in" : (0, 100, 20, 100, 102.689, 11.741),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_5r1_5x2_6 = {
    "in" : (0, 100, 20, 100.0000001, 97.014, 15.028),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_5r1_5x2_7 = {
    "in" : (0, 100, 20, 103.678, 25.098, 17.069),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_5r1_6 = {
    "in" : (0, 100, 20.0000001, 95.216, 81.522, 8.343),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_5r1_7 = {
    "in" : (0, 100, 22.726, 12.394, 92.427, 18.933),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_6 = {
    "in" : (0, 100.0000001, 3.128, 41.527, 14.405, 19.134),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_3y1_7 = {
    "in" : (0, 102.903, 18.016, 45.115, 1.963, 3.018),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_1 = {
    "in" : (100, -2.397, 2.252, 76.597, 45.682, 16.011),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_2 = {
    "in" : (100, -1e-07, 16.488, 49.325, 39.441, 4.595),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_3r1_1 = {
    "in" : (100, 0, -2.319, 11.468, 44.264, 19.606),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_3r1_2 = {
    "in" : (100, 0, 0.9999999, 27.353, 17.22, 14.777),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_3r1_3x2_1 = {
    "in" : (100, 0, 1, -3.216, 67.363, 3.216),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_3r1_3x2_2 = {
    "in" : (100, 0, 1, -1e-07, 27.049, 14.268),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_3r1_3x2_3y2_1 = {
    "in" : (100, 0, 1, 0, -3.569, 2.52),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_3r1_3x2_3y2_2 = {
    "in" : (100, 0, 1, 0, -1e-07, 18.671),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_3r1_3x2_3y2_3r2_1 = {
    "in" : (100, 0, 1, 0, 0, -1.261),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_3r1_3x2_3y2_3r2_2 = {
    "in" : (100, 0, 1, 0, 0, 0.9999999),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_3r1_3x2_3y2_3r2_3 = {
    "in" : (100, 0, 1, 0, 0, 1),
    "out" : False
}
        
collision_x1_5y1_3r1_3x2_3y2_3r2_5 = {
    "in" : (100, 0, 1, 0, 0, 20),
    "out" : False
}
        
collision_x1_5y1_3r1_3x2_3y2_3r2_6 = {
    "in" : (100, 0, 1, 0, 0, 20.0000001),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_3r1_3x2_3y2_3r2_7 = {
    "in" : (100, 0, 1, 0, 0, 22.647),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_3r1_3x2_3y2_5r2_1 = {
    "in" : (100, 0, 1, 0, 100, -2.108),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_3r1_3x2_3y2_5r2_2 = {
    "in" : (100, 0, 1, 0, 100, 0.9999999),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_3r1_3x2_3y2_5r2_3 = {
    "in" : (100, 0, 1, 0, 100, 1),
    "out" : False
}
        
collision_x1_5y1_3r1_3x2_3y2_5r2_5 = {
    "in" : (100, 0, 1, 0, 100, 20),
    "out" : False
}
        
collision_x1_5y1_3r1_3x2_3y2_5r2_6 = {
    "in" : (100, 0, 1, 0, 100, 20.0000001),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_3r1_3x2_3y2_5r2_7 = {
    "in" : (100, 0, 1, 0, 100, 23.579),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_3r1_3x2_3y2_6 = {
    "in" : (100, 0, 1, 0, 100.0000001, 19.428),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_3r1_3x2_3y2_7 = {
    "in" : (100, 0, 1, 0, 103.01, 8.996),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_3r1_3x2_5y2_1 = {
    "in" : (100, 0, 1, 100, -3.137, 10.597),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_3r1_3x2_5y2_2 = {
    "in" : (100, 0, 1, 100, -1e-07, 6.48),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_3r1_3x2_5y2_3r2_1 = {
    "in" : (100, 0, 1, 100, 0, -1.828),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_3r1_3x2_5y2_3r2_2 = {
    "in" : (100, 0, 1, 100, 0, 0.9999999),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_3r1_3x2_5y2_3r2_3 = {
    "in" : (100, 0, 1, 100, 0, 1),
    "out" : True
}
        
collision_x1_5y1_3r1_3x2_5y2_3r2_5 = {
    "in" : (100, 0, 1, 100, 0, 20),
    "out" : True
}
        
collision_x1_5y1_3r1_3x2_5y2_3r2_6 = {
    "in" : (100, 0, 1, 100, 0, 20.0000001),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_3r1_3x2_5y2_3r2_7 = {
    "in" : (100, 0, 1, 100, 0, 23.604),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_3r1_3x2_5y2_5r2_1 = {
    "in" : (100, 0, 1, 100, 100, -1.144),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_3r1_3x2_5y2_5r2_2 = {
    "in" : (100, 0, 1, 100, 100, 0.9999999),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_3r1_3x2_5y2_5r2_3 = {
    "in" : (100, 0, 1, 100, 100, 1),
    "out" : False
}
        
collision_x1_5y1_3r1_3x2_5y2_5r2_5 = {
    "in" : (100, 0, 1, 100, 100, 20),
    "out" : False
}
        
collision_x1_5y1_3r1_3x2_5y2_5r2_6 = {
    "in" : (100, 0, 1, 100, 100, 20.0000001),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_3r1_3x2_5y2_5r2_7 = {
    "in" : (100, 0, 1, 100, 100, 22.749),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_3r1_3x2_5y2_6 = {
    "in" : (100, 0, 1, 100, 100.0000001, 5.965),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_3r1_3x2_5y2_7 = {
    "in" : (100, 0, 1, 100, 103.51, 1.092),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_3r1_3x2_6 = {
    "in" : (100, 0, 1, 100.0000001, 28.643, 7.704),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_3r1_3x2_7 = {
    "in" : (100, 0, 1, 103.67, 70.114, 10.451),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_3r1_5x2_1 = {
    "in" : (100, 0, 20, -3.978, 49.041, 15.425),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_3r1_5x2_2 = {
    "in" : (100, 0, 20, -1e-07, 84.391, 18.117),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_3r1_5x2_3y2_1 = {
    "in" : (100, 0, 20, 0, -3.626, 18.339),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_3r1_5x2_3y2_2 = {
    "in" : (100, 0, 20, 0, -1e-07, 2.814),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_3r1_5x2_3y2_3r2_1 = {
    "in" : (100, 0, 20, 0, 0, -1.012),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_3r1_5x2_3y2_3r2_2 = {
    "in" : (100, 0, 20, 0, 0, 0.9999999),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_3r1_5x2_3y2_3r2_3 = {
    "in" : (100, 0, 20, 0, 0, 1),
    "out" : False
}
        
collision_x1_5y1_3r1_5x2_3y2_3r2_5 = {
    "in" : (100, 0, 20, 0, 0, 20),
    "out" : False
}
        
collision_x1_5y1_3r1_5x2_3y2_3r2_6 = {
    "in" : (100, 0, 20, 0, 0, 20.0000001),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_3r1_5x2_3y2_3r2_7 = {
    "in" : (100, 0, 20, 0, 0, 23.159),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_3r1_5x2_3y2_5r2_1 = {
    "in" : (100, 0, 20, 0, 100, -2.487),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_3r1_5x2_3y2_5r2_2 = {
    "in" : (100, 0, 20, 0, 100, 0.9999999),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_3r1_5x2_3y2_5r2_3 = {
    "in" : (100, 0, 20, 0, 100, 1),
    "out" : False
}
        
collision_x1_5y1_3r1_5x2_3y2_5r2_5 = {
    "in" : (100, 0, 20, 0, 100, 20),
    "out" : False
}
        
collision_x1_5y1_3r1_5x2_3y2_5r2_6 = {
    "in" : (100, 0, 20, 0, 100, 20.0000001),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_3r1_5x2_3y2_5r2_7 = {
    "in" : (100, 0, 20, 0, 100, 22.803),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_3r1_5x2_3y2_6 = {
    "in" : (100, 0, 20, 0, 100.0000001, 8.502),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_3r1_5x2_3y2_7 = {
    "in" : (100, 0, 20, 0, 102.314, 15.956),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_3r1_5x2_5y2_1 = {
    "in" : (100, 0, 20, 100, -3.128, 6.197),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_3r1_5x2_5y2_2 = {
    "in" : (100, 0, 20, 100, -1e-07, 13.281),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_3r1_5x2_5y2_3r2_1 = {
    "in" : (100, 0, 20, 100, 0, -2.401),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_3r1_5x2_5y2_3r2_2 = {
    "in" : (100, 0, 20, 100, 0, 0.9999999),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_3r1_5x2_5y2_3r2_3 = {
    "in" : (100, 0, 20, 100, 0, 1),
    "out" : True
}
        
collision_x1_5y1_3r1_5x2_5y2_3r2_5 = {
    "in" : (100, 0, 20, 100, 0, 20),
    "out" : True
}
        
collision_x1_5y1_3r1_5x2_5y2_3r2_6 = {
    "in" : (100, 0, 20, 100, 0, 20.0000001),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_3r1_5x2_5y2_3r2_7 = {
    "in" : (100, 0, 20, 100, 0, 22.21),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_3r1_5x2_5y2_5r2_1 = {
    "in" : (100, 0, 20, 100, 100, -2.989),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_3r1_5x2_5y2_5r2_2 = {
    "in" : (100, 0, 20, 100, 100, 0.9999999),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_3r1_5x2_5y2_5r2_3 = {
    "in" : (100, 0, 20, 100, 100, 1),
    "out" : False
}
        
collision_x1_5y1_3r1_5x2_5y2_5r2_5 = {
    "in" : (100, 0, 20, 100, 100, 20),
    "out" : False
}
        
collision_x1_5y1_3r1_5x2_5y2_5r2_6 = {
    "in" : (100, 0, 20, 100, 100, 20.0000001),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_3r1_5x2_5y2_5r2_7 = {
    "in" : (100, 0, 20, 100, 100, 23.053),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_3r1_5x2_5y2_6 = {
    "in" : (100, 0, 20, 100, 100.0000001, 17.82),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_3r1_5x2_5y2_7 = {
    "in" : (100, 0, 20, 100, 103.263, 18.991),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_3r1_5x2_6 = {
    "in" : (100, 0, 20, 100.0000001, 55.949, 4.711),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_3r1_5x2_7 = {
    "in" : (100, 0, 20, 102.841, 1.557, 17.606),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_3r1_6 = {
    "in" : (100, 0, 20.0000001, 10.586, 81.377, 19.354),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_3r1_7 = {
    "in" : (100, 0, 23.64, 94.99, 9.184, 11.73),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_5r1_1 = {
    "in" : (100, 100, -1.084, 32.04, 30.367, 5.954),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_5r1_2 = {
    "in" : (100, 100, 0.9999999, 81.539, 72.67, 2.114),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_5r1_3x2_1 = {
    "in" : (100, 100, 1, -2.021, 26.732, 9.32),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_5r1_3x2_2 = {
    "in" : (100, 100, 1, -1e-07, 46.124, 5.7),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_5r1_3x2_3y2_1 = {
    "in" : (100, 100, 1, 0, -3.162, 2.724),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_5r1_3x2_3y2_2 = {
    "in" : (100, 100, 1, 0, -1e-07, 8.565),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_5r1_3x2_3y2_3r2_1 = {
    "in" : (100, 100, 1, 0, 0, -2.147),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_5r1_3x2_3y2_3r2_2 = {
    "in" : (100, 100, 1, 0, 0, 0.9999999),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_5r1_3x2_3y2_3r2_3 = {
    "in" : (100, 100, 1, 0, 0, 1),
    "out" : False
}
        
collision_x1_5y1_5r1_3x2_3y2_3r2_5 = {
    "in" : (100, 100, 1, 0, 0, 20),
    "out" : False
}
        
collision_x1_5y1_5r1_3x2_3y2_3r2_6 = {
    "in" : (100, 100, 1, 0, 0, 20.0000001),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_5r1_3x2_3y2_3r2_7 = {
    "in" : (100, 100, 1, 0, 0, 23.433),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_5r1_3x2_3y2_5r2_1 = {
    "in" : (100, 100, 1, 0, 100, -1.461),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_5r1_3x2_3y2_5r2_2 = {
    "in" : (100, 100, 1, 0, 100, 0.9999999),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_5r1_3x2_3y2_5r2_3 = {
    "in" : (100, 100, 1, 0, 100, 1),
    "out" : False
}
        
collision_x1_5y1_5r1_3x2_3y2_5r2_5 = {
    "in" : (100, 100, 1, 0, 100, 20),
    "out" : False
}
        
collision_x1_5y1_5r1_3x2_3y2_5r2_6 = {
    "in" : (100, 100, 1, 0, 100, 20.0000001),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_5r1_3x2_3y2_5r2_7 = {
    "in" : (100, 100, 1, 0, 100, 23.011),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_5r1_3x2_3y2_6 = {
    "in" : (100, 100, 1, 0, 100.0000001, 17.86),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_5r1_3x2_3y2_7 = {
    "in" : (100, 100, 1, 0, 102.402, 14.843),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_5r1_3x2_5y2_1 = {
    "in" : (100, 100, 1, 100, -3.743, 3.027),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_5r1_3x2_5y2_2 = {
    "in" : (100, 100, 1, 100, -1e-07, 10.696),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_5r1_3x2_5y2_3r2_1 = {
    "in" : (100, 100, 1, 100, 0, -2.872),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_5r1_3x2_5y2_3r2_2 = {
    "in" : (100, 100, 1, 100, 0, 0.9999999),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_5r1_3x2_5y2_3r2_3 = {
    "in" : (100, 100, 1, 100, 0, 1),
    "out" : False
}
        
collision_x1_5y1_5r1_3x2_5y2_3r2_5 = {
    "in" : (100, 100, 1, 100, 0, 20),
    "out" : False
}
        
collision_x1_5y1_5r1_3x2_5y2_3r2_6 = {
    "in" : (100, 100, 1, 100, 0, 20.0000001),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_5r1_3x2_5y2_3r2_7 = {
    "in" : (100, 100, 1, 100, 0, 22.979),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_5r1_3x2_5y2_5r2_1 = {
    "in" : (100, 100, 1, 100, 100, -2.406),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_5r1_3x2_5y2_5r2_2 = {
    "in" : (100, 100, 1, 100, 100, 0.9999999),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_5r1_3x2_5y2_5r2_3 = {
    "in" : (100, 100, 1, 100, 100, 1),
    "out" : True
}
        
collision_x1_5y1_5r1_3x2_5y2_5r2_5 = {
    "in" : (100, 100, 1, 100, 100, 20),
    "out" : True
}
        
collision_x1_5y1_5r1_3x2_5y2_5r2_6 = {
    "in" : (100, 100, 1, 100, 100, 20.0000001),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_5r1_3x2_5y2_5r2_7 = {
    "in" : (100, 100, 1, 100, 100, 23.824),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_5r1_3x2_5y2_6 = {
    "in" : (100, 100, 1, 100, 100.0000001, 2.939),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_5r1_3x2_5y2_7 = {
    "in" : (100, 100, 1, 100, 103.705, 4.112),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_5r1_3x2_6 = {
    "in" : (100, 100, 1, 100.0000001, 56.112, 11.848),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_5r1_3x2_7 = {
    "in" : (100, 100, 1, 103.303, 66.254, 16.827),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_5r1_5x2_1 = {
    "in" : (100, 100, 20, -3.122, 79.213, 13.39),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_5r1_5x2_2 = {
    "in" : (100, 100, 20, -1e-07, 69.894, 11.243),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_5r1_5x2_3y2_1 = {
    "in" : (100, 100, 20, 0, -2.251, 3.034),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_5r1_5x2_3y2_2 = {
    "in" : (100, 100, 20, 0, -1e-07, 17.73),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_5r1_5x2_3y2_3r2_1 = {
    "in" : (100, 100, 20, 0, 0, -1.817),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_5r1_5x2_3y2_3r2_2 = {
    "in" : (100, 100, 20, 0, 0, 0.9999999),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_5r1_5x2_3y2_3r2_3 = {
    "in" : (100, 100, 20, 0, 0, 1),
    "out" : False
}
        
collision_x1_5y1_5r1_5x2_3y2_3r2_5 = {
    "in" : (100, 100, 20, 0, 0, 20),
    "out" : False
}
        
collision_x1_5y1_5r1_5x2_3y2_3r2_6 = {
    "in" : (100, 100, 20, 0, 0, 20.0000001),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_5r1_5x2_3y2_3r2_7 = {
    "in" : (100, 100, 20, 0, 0, 22.191),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_5r1_5x2_3y2_5r2_1 = {
    "in" : (100, 100, 20, 0, 100, -2.301),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_5r1_5x2_3y2_5r2_2 = {
    "in" : (100, 100, 20, 0, 100, 0.9999999),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_5r1_5x2_3y2_5r2_3 = {
    "in" : (100, 100, 20, 0, 100, 1),
    "out" : False
}
        
collision_x1_5y1_5r1_5x2_3y2_5r2_5 = {
    "in" : (100, 100, 20, 0, 100, 20),
    "out" : False
}
        
collision_x1_5y1_5r1_5x2_3y2_5r2_6 = {
    "in" : (100, 100, 20, 0, 100, 20.0000001),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_5r1_5x2_3y2_5r2_7 = {
    "in" : (100, 100, 20, 0, 100, 23.441),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_5r1_5x2_3y2_6 = {
    "in" : (100, 100, 20, 0, 100.0000001, 9.56),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_5r1_5x2_3y2_7 = {
    "in" : (100, 100, 20, 0, 102.81, 10.992),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_5r1_5x2_5y2_1 = {
    "in" : (100, 100, 20, 100, -2.069, 6.173),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_5r1_5x2_5y2_2 = {
    "in" : (100, 100, 20, 100, -1e-07, 6.909),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_5r1_5x2_5y2_3r2_1 = {
    "in" : (100, 100, 20, 100, 0, -2.437),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_5r1_5x2_5y2_3r2_2 = {
    "in" : (100, 100, 20, 100, 0, 0.9999999),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_5r1_5x2_5y2_3r2_3 = {
    "in" : (100, 100, 20, 100, 0, 1),
    "out" : False
}
        
collision_x1_5y1_5r1_5x2_5y2_3r2_5 = {
    "in" : (100, 100, 20, 100, 0, 20),
    "out" : False
}
        
collision_x1_5y1_5r1_5x2_5y2_3r2_6 = {
    "in" : (100, 100, 20, 100, 0, 20.0000001),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_5r1_5x2_5y2_3r2_7 = {
    "in" : (100, 100, 20, 100, 0, 22.482),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_5r1_5x2_5y2_5r2_1 = {
    "in" : (100, 100, 20, 100, 100, -1.898),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_5r1_5x2_5y2_5r2_2 = {
    "in" : (100, 100, 20, 100, 100, 0.9999999),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_5r1_5x2_5y2_5r2_3 = {
    "in" : (100, 100, 20, 100, 100, 1),
    "out" : True
}
        
collision_x1_5y1_5r1_5x2_5y2_5r2_5 = {
    "in" : (100, 100, 20, 100, 100, 20),
    "out" : True
}
        
collision_x1_5y1_5r1_5x2_5y2_5r2_6 = {
    "in" : (100, 100, 20, 100, 100, 20.0000001),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_5r1_5x2_5y2_5r2_7 = {
    "in" : (100, 100, 20, 100, 100, 22.858),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_5r1_5x2_5y2_6 = {
    "in" : (100, 100, 20, 100, 100.0000001, 5.869),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_5r1_5x2_5y2_7 = {
    "in" : (100, 100, 20, 100, 102.479, 16.359),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_5r1_5x2_6 = {
    "in" : (100, 100, 20, 100.0000001, 82.988, 3.499),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_5r1_5x2_7 = {
    "in" : (100, 100, 20, 102.874, 22.457, 2.937),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_5r1_6 = {
    "in" : (100, 100, 20.0000001, 23.856, 59.626, 8.636),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_5r1_7 = {
    "in" : (100, 100, 22.044, 10.513, 2.054, 11.989),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_6 = {
    "in" : (100, 100.0000001, 19.728, 46.799, 37.173, 14.053),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_5y1_7 = {
    "in" : (100, 102.349, 15.667, 35.615, 42.963, 3.395),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_6 = {
    "in" : (100.0000001, 51.283, 18.329, 97.274, 54.353, 9.291),
    "out" : ERR_OUT_OF_BOUNDS
}
        
collision_x1_7 = {
    "in" : (103.046, 55.533, 15.901, 4.357, 60.823, 2.505),
    "out" : ERR_OUT_OF_BOUNDS
}

class TestCollision(unittest.TestCase):

    def test_collision_x1_1(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_1["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_1["out"])

    def test_collision_x1_2(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_2["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_2["out"])

    def test_collision_x1_3y1_1(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_1["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_1["out"])

    def test_collision_x1_3y1_2(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_2["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_2["out"])

    def test_collision_x1_3y1_3r1_1(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_3r1_1["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_3r1_1["out"])

    def test_collision_x1_3y1_3r1_2(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_3r1_2["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_3r1_2["out"])

    def test_collision_x1_3y1_3r1_3x2_1(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_3r1_3x2_1["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_3r1_3x2_1["out"])

    def test_collision_x1_3y1_3r1_3x2_2(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_3r1_3x2_2["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_3r1_3x2_2["out"])

    def test_collision_x1_3y1_3r1_3x2_3y2_1(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_3r1_3x2_3y2_1["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_3r1_3x2_3y2_1["out"])

    def test_collision_x1_3y1_3r1_3x2_3y2_2(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_3r1_3x2_3y2_2["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_3r1_3x2_3y2_2["out"])

    def test_collision_x1_3y1_3r1_3x2_3y2_3r2_1(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_3r1_3x2_3y2_3r2_1["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_3r1_3x2_3y2_3r2_1["out"])

    def test_collision_x1_3y1_3r1_3x2_3y2_3r2_2(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_3r1_3x2_3y2_3r2_2["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_3r1_3x2_3y2_3r2_2["out"])

    def test_collision_x1_3y1_3r1_3x2_3y2_3r2_3(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_3r1_3x2_3y2_3r2_3["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_3r1_3x2_3y2_3r2_3["out"])

    def test_collision_x1_3y1_3r1_3x2_3y2_3r2_5(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_3r1_3x2_3y2_3r2_5["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_3r1_3x2_3y2_3r2_5["out"])

    def test_collision_x1_3y1_3r1_3x2_3y2_3r2_6(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_3r1_3x2_3y2_3r2_6["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_3r1_3x2_3y2_3r2_6["out"])

    def test_collision_x1_3y1_3r1_3x2_3y2_3r2_7(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_3r1_3x2_3y2_3r2_7["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_3r1_3x2_3y2_3r2_7["out"])

    def test_collision_x1_3y1_3r1_3x2_3y2_5r2_1(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_3r1_3x2_3y2_5r2_1["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_3r1_3x2_3y2_5r2_1["out"])

    def test_collision_x1_3y1_3r1_3x2_3y2_5r2_2(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_3r1_3x2_3y2_5r2_2["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_3r1_3x2_3y2_5r2_2["out"])

    def test_collision_x1_3y1_3r1_3x2_3y2_5r2_3(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_3r1_3x2_3y2_5r2_3["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_3r1_3x2_3y2_5r2_3["out"])

    def test_collision_x1_3y1_3r1_3x2_3y2_5r2_5(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_3r1_3x2_3y2_5r2_5["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_3r1_3x2_3y2_5r2_5["out"])

    def test_collision_x1_3y1_3r1_3x2_3y2_5r2_6(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_3r1_3x2_3y2_5r2_6["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_3r1_3x2_3y2_5r2_6["out"])

    def test_collision_x1_3y1_3r1_3x2_3y2_5r2_7(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_3r1_3x2_3y2_5r2_7["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_3r1_3x2_3y2_5r2_7["out"])

    def test_collision_x1_3y1_3r1_3x2_3y2_6(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_3r1_3x2_3y2_6["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_3r1_3x2_3y2_6["out"])

    def test_collision_x1_3y1_3r1_3x2_3y2_7(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_3r1_3x2_3y2_7["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_3r1_3x2_3y2_7["out"])

    def test_collision_x1_3y1_3r1_3x2_5y2_1(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_3r1_3x2_5y2_1["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_3r1_3x2_5y2_1["out"])

    def test_collision_x1_3y1_3r1_3x2_5y2_2(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_3r1_3x2_5y2_2["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_3r1_3x2_5y2_2["out"])

    def test_collision_x1_3y1_3r1_3x2_5y2_3r2_1(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_3r1_3x2_5y2_3r2_1["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_3r1_3x2_5y2_3r2_1["out"])

    def test_collision_x1_3y1_3r1_3x2_5y2_3r2_2(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_3r1_3x2_5y2_3r2_2["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_3r1_3x2_5y2_3r2_2["out"])

    def test_collision_x1_3y1_3r1_3x2_5y2_3r2_3(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_3r1_3x2_5y2_3r2_3["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_3r1_3x2_5y2_3r2_3["out"])

    def test_collision_x1_3y1_3r1_3x2_5y2_3r2_5(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_3r1_3x2_5y2_3r2_5["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_3r1_3x2_5y2_3r2_5["out"])

    def test_collision_x1_3y1_3r1_3x2_5y2_3r2_6(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_3r1_3x2_5y2_3r2_6["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_3r1_3x2_5y2_3r2_6["out"])

    def test_collision_x1_3y1_3r1_3x2_5y2_3r2_7(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_3r1_3x2_5y2_3r2_7["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_3r1_3x2_5y2_3r2_7["out"])

    def test_collision_x1_3y1_3r1_3x2_5y2_5r2_1(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_3r1_3x2_5y2_5r2_1["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_3r1_3x2_5y2_5r2_1["out"])

    def test_collision_x1_3y1_3r1_3x2_5y2_5r2_2(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_3r1_3x2_5y2_5r2_2["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_3r1_3x2_5y2_5r2_2["out"])

    def test_collision_x1_3y1_3r1_3x2_5y2_5r2_3(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_3r1_3x2_5y2_5r2_3["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_3r1_3x2_5y2_5r2_3["out"])

    def test_collision_x1_3y1_3r1_3x2_5y2_5r2_5(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_3r1_3x2_5y2_5r2_5["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_3r1_3x2_5y2_5r2_5["out"])

    def test_collision_x1_3y1_3r1_3x2_5y2_5r2_6(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_3r1_3x2_5y2_5r2_6["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_3r1_3x2_5y2_5r2_6["out"])

    def test_collision_x1_3y1_3r1_3x2_5y2_5r2_7(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_3r1_3x2_5y2_5r2_7["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_3r1_3x2_5y2_5r2_7["out"])

    def test_collision_x1_3y1_3r1_3x2_5y2_6(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_3r1_3x2_5y2_6["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_3r1_3x2_5y2_6["out"])

    def test_collision_x1_3y1_3r1_3x2_5y2_7(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_3r1_3x2_5y2_7["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_3r1_3x2_5y2_7["out"])

    def test_collision_x1_3y1_3r1_3x2_6(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_3r1_3x2_6["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_3r1_3x2_6["out"])

    def test_collision_x1_3y1_3r1_3x2_7(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_3r1_3x2_7["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_3r1_3x2_7["out"])

    def test_collision_x1_3y1_3r1_5x2_1(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_3r1_5x2_1["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_3r1_5x2_1["out"])

    def test_collision_x1_3y1_3r1_5x2_2(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_3r1_5x2_2["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_3r1_5x2_2["out"])

    def test_collision_x1_3y1_3r1_5x2_3y2_1(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_3r1_5x2_3y2_1["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_3r1_5x2_3y2_1["out"])

    def test_collision_x1_3y1_3r1_5x2_3y2_2(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_3r1_5x2_3y2_2["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_3r1_5x2_3y2_2["out"])

    def test_collision_x1_3y1_3r1_5x2_3y2_3r2_1(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_3r1_5x2_3y2_3r2_1["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_3r1_5x2_3y2_3r2_1["out"])

    def test_collision_x1_3y1_3r1_5x2_3y2_3r2_2(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_3r1_5x2_3y2_3r2_2["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_3r1_5x2_3y2_3r2_2["out"])

    def test_collision_x1_3y1_3r1_5x2_3y2_3r2_3(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_3r1_5x2_3y2_3r2_3["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_3r1_5x2_3y2_3r2_3["out"])

    def test_collision_x1_3y1_3r1_5x2_3y2_3r2_5(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_3r1_5x2_3y2_3r2_5["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_3r1_5x2_3y2_3r2_5["out"])

    def test_collision_x1_3y1_3r1_5x2_3y2_3r2_6(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_3r1_5x2_3y2_3r2_6["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_3r1_5x2_3y2_3r2_6["out"])

    def test_collision_x1_3y1_3r1_5x2_3y2_3r2_7(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_3r1_5x2_3y2_3r2_7["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_3r1_5x2_3y2_3r2_7["out"])

    def test_collision_x1_3y1_3r1_5x2_3y2_5r2_1(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_3r1_5x2_3y2_5r2_1["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_3r1_5x2_3y2_5r2_1["out"])

    def test_collision_x1_3y1_3r1_5x2_3y2_5r2_2(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_3r1_5x2_3y2_5r2_2["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_3r1_5x2_3y2_5r2_2["out"])

    def test_collision_x1_3y1_3r1_5x2_3y2_5r2_3(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_3r1_5x2_3y2_5r2_3["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_3r1_5x2_3y2_5r2_3["out"])

    def test_collision_x1_3y1_3r1_5x2_3y2_5r2_5(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_3r1_5x2_3y2_5r2_5["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_3r1_5x2_3y2_5r2_5["out"])

    def test_collision_x1_3y1_3r1_5x2_3y2_5r2_6(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_3r1_5x2_3y2_5r2_6["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_3r1_5x2_3y2_5r2_6["out"])

    def test_collision_x1_3y1_3r1_5x2_3y2_5r2_7(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_3r1_5x2_3y2_5r2_7["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_3r1_5x2_3y2_5r2_7["out"])

    def test_collision_x1_3y1_3r1_5x2_3y2_6(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_3r1_5x2_3y2_6["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_3r1_5x2_3y2_6["out"])

    def test_collision_x1_3y1_3r1_5x2_3y2_7(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_3r1_5x2_3y2_7["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_3r1_5x2_3y2_7["out"])

    def test_collision_x1_3y1_3r1_5x2_5y2_1(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_3r1_5x2_5y2_1["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_3r1_5x2_5y2_1["out"])

    def test_collision_x1_3y1_3r1_5x2_5y2_2(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_3r1_5x2_5y2_2["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_3r1_5x2_5y2_2["out"])

    def test_collision_x1_3y1_3r1_5x2_5y2_3r2_1(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_3r1_5x2_5y2_3r2_1["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_3r1_5x2_5y2_3r2_1["out"])

    def test_collision_x1_3y1_3r1_5x2_5y2_3r2_2(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_3r1_5x2_5y2_3r2_2["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_3r1_5x2_5y2_3r2_2["out"])

    def test_collision_x1_3y1_3r1_5x2_5y2_3r2_3(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_3r1_5x2_5y2_3r2_3["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_3r1_5x2_5y2_3r2_3["out"])

    def test_collision_x1_3y1_3r1_5x2_5y2_3r2_5(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_3r1_5x2_5y2_3r2_5["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_3r1_5x2_5y2_3r2_5["out"])

    def test_collision_x1_3y1_3r1_5x2_5y2_3r2_6(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_3r1_5x2_5y2_3r2_6["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_3r1_5x2_5y2_3r2_6["out"])

    def test_collision_x1_3y1_3r1_5x2_5y2_3r2_7(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_3r1_5x2_5y2_3r2_7["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_3r1_5x2_5y2_3r2_7["out"])

    def test_collision_x1_3y1_3r1_5x2_5y2_5r2_1(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_3r1_5x2_5y2_5r2_1["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_3r1_5x2_5y2_5r2_1["out"])

    def test_collision_x1_3y1_3r1_5x2_5y2_5r2_2(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_3r1_5x2_5y2_5r2_2["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_3r1_5x2_5y2_5r2_2["out"])

    def test_collision_x1_3y1_3r1_5x2_5y2_5r2_3(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_3r1_5x2_5y2_5r2_3["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_3r1_5x2_5y2_5r2_3["out"])

    def test_collision_x1_3y1_3r1_5x2_5y2_5r2_5(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_3r1_5x2_5y2_5r2_5["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_3r1_5x2_5y2_5r2_5["out"])

    def test_collision_x1_3y1_3r1_5x2_5y2_5r2_6(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_3r1_5x2_5y2_5r2_6["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_3r1_5x2_5y2_5r2_6["out"])

    def test_collision_x1_3y1_3r1_5x2_5y2_5r2_7(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_3r1_5x2_5y2_5r2_7["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_3r1_5x2_5y2_5r2_7["out"])

    def test_collision_x1_3y1_3r1_5x2_5y2_6(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_3r1_5x2_5y2_6["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_3r1_5x2_5y2_6["out"])

    def test_collision_x1_3y1_3r1_5x2_5y2_7(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_3r1_5x2_5y2_7["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_3r1_5x2_5y2_7["out"])

    def test_collision_x1_3y1_3r1_5x2_6(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_3r1_5x2_6["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_3r1_5x2_6["out"])

    def test_collision_x1_3y1_3r1_5x2_7(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_3r1_5x2_7["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_3r1_5x2_7["out"])

    def test_collision_x1_3y1_3r1_6(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_3r1_6["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_3r1_6["out"])

    def test_collision_x1_3y1_3r1_7(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_3r1_7["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_3r1_7["out"])

    def test_collision_x1_3y1_5r1_1(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_5r1_1["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_5r1_1["out"])

    def test_collision_x1_3y1_5r1_2(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_5r1_2["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_5r1_2["out"])

    def test_collision_x1_3y1_5r1_3x2_1(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_5r1_3x2_1["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_5r1_3x2_1["out"])

    def test_collision_x1_3y1_5r1_3x2_2(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_5r1_3x2_2["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_5r1_3x2_2["out"])

    def test_collision_x1_3y1_5r1_3x2_3y2_1(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_5r1_3x2_3y2_1["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_5r1_3x2_3y2_1["out"])

    def test_collision_x1_3y1_5r1_3x2_3y2_2(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_5r1_3x2_3y2_2["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_5r1_3x2_3y2_2["out"])

    def test_collision_x1_3y1_5r1_3x2_3y2_3r2_1(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_5r1_3x2_3y2_3r2_1["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_5r1_3x2_3y2_3r2_1["out"])

    def test_collision_x1_3y1_5r1_3x2_3y2_3r2_2(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_5r1_3x2_3y2_3r2_2["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_5r1_3x2_3y2_3r2_2["out"])

    def test_collision_x1_3y1_5r1_3x2_3y2_3r2_3(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_5r1_3x2_3y2_3r2_3["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_5r1_3x2_3y2_3r2_3["out"])

    def test_collision_x1_3y1_5r1_3x2_3y2_3r2_5(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_5r1_3x2_3y2_3r2_5["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_5r1_3x2_3y2_3r2_5["out"])

    def test_collision_x1_3y1_5r1_3x2_3y2_3r2_6(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_5r1_3x2_3y2_3r2_6["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_5r1_3x2_3y2_3r2_6["out"])

    def test_collision_x1_3y1_5r1_3x2_3y2_3r2_7(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_5r1_3x2_3y2_3r2_7["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_5r1_3x2_3y2_3r2_7["out"])

    def test_collision_x1_3y1_5r1_3x2_3y2_5r2_1(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_5r1_3x2_3y2_5r2_1["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_5r1_3x2_3y2_5r2_1["out"])

    def test_collision_x1_3y1_5r1_3x2_3y2_5r2_2(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_5r1_3x2_3y2_5r2_2["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_5r1_3x2_3y2_5r2_2["out"])

    def test_collision_x1_3y1_5r1_3x2_3y2_5r2_3(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_5r1_3x2_3y2_5r2_3["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_5r1_3x2_3y2_5r2_3["out"])

    def test_collision_x1_3y1_5r1_3x2_3y2_5r2_5(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_5r1_3x2_3y2_5r2_5["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_5r1_3x2_3y2_5r2_5["out"])

    def test_collision_x1_3y1_5r1_3x2_3y2_5r2_6(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_5r1_3x2_3y2_5r2_6["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_5r1_3x2_3y2_5r2_6["out"])

    def test_collision_x1_3y1_5r1_3x2_3y2_5r2_7(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_5r1_3x2_3y2_5r2_7["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_5r1_3x2_3y2_5r2_7["out"])

    def test_collision_x1_3y1_5r1_3x2_3y2_6(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_5r1_3x2_3y2_6["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_5r1_3x2_3y2_6["out"])

    def test_collision_x1_3y1_5r1_3x2_3y2_7(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_5r1_3x2_3y2_7["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_5r1_3x2_3y2_7["out"])

    def test_collision_x1_3y1_5r1_3x2_5y2_1(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_5r1_3x2_5y2_1["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_5r1_3x2_5y2_1["out"])

    def test_collision_x1_3y1_5r1_3x2_5y2_2(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_5r1_3x2_5y2_2["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_5r1_3x2_5y2_2["out"])

    def test_collision_x1_3y1_5r1_3x2_5y2_3r2_1(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_5r1_3x2_5y2_3r2_1["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_5r1_3x2_5y2_3r2_1["out"])

    def test_collision_x1_3y1_5r1_3x2_5y2_3r2_2(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_5r1_3x2_5y2_3r2_2["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_5r1_3x2_5y2_3r2_2["out"])

    def test_collision_x1_3y1_5r1_3x2_5y2_3r2_3(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_5r1_3x2_5y2_3r2_3["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_5r1_3x2_5y2_3r2_3["out"])

    def test_collision_x1_3y1_5r1_3x2_5y2_3r2_5(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_5r1_3x2_5y2_3r2_5["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_5r1_3x2_5y2_3r2_5["out"])

    def test_collision_x1_3y1_5r1_3x2_5y2_3r2_6(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_5r1_3x2_5y2_3r2_6["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_5r1_3x2_5y2_3r2_6["out"])

    def test_collision_x1_3y1_5r1_3x2_5y2_3r2_7(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_5r1_3x2_5y2_3r2_7["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_5r1_3x2_5y2_3r2_7["out"])

    def test_collision_x1_3y1_5r1_3x2_5y2_5r2_1(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_5r1_3x2_5y2_5r2_1["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_5r1_3x2_5y2_5r2_1["out"])

    def test_collision_x1_3y1_5r1_3x2_5y2_5r2_2(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_5r1_3x2_5y2_5r2_2["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_5r1_3x2_5y2_5r2_2["out"])

    def test_collision_x1_3y1_5r1_3x2_5y2_5r2_3(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_5r1_3x2_5y2_5r2_3["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_5r1_3x2_5y2_5r2_3["out"])

    def test_collision_x1_3y1_5r1_3x2_5y2_5r2_5(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_5r1_3x2_5y2_5r2_5["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_5r1_3x2_5y2_5r2_5["out"])

    def test_collision_x1_3y1_5r1_3x2_5y2_5r2_6(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_5r1_3x2_5y2_5r2_6["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_5r1_3x2_5y2_5r2_6["out"])

    def test_collision_x1_3y1_5r1_3x2_5y2_5r2_7(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_5r1_3x2_5y2_5r2_7["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_5r1_3x2_5y2_5r2_7["out"])

    def test_collision_x1_3y1_5r1_3x2_5y2_6(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_5r1_3x2_5y2_6["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_5r1_3x2_5y2_6["out"])

    def test_collision_x1_3y1_5r1_3x2_5y2_7(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_5r1_3x2_5y2_7["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_5r1_3x2_5y2_7["out"])

    def test_collision_x1_3y1_5r1_3x2_6(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_5r1_3x2_6["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_5r1_3x2_6["out"])

    def test_collision_x1_3y1_5r1_3x2_7(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_5r1_3x2_7["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_5r1_3x2_7["out"])

    def test_collision_x1_3y1_5r1_5x2_1(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_5r1_5x2_1["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_5r1_5x2_1["out"])

    def test_collision_x1_3y1_5r1_5x2_2(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_5r1_5x2_2["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_5r1_5x2_2["out"])

    def test_collision_x1_3y1_5r1_5x2_3y2_1(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_5r1_5x2_3y2_1["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_5r1_5x2_3y2_1["out"])

    def test_collision_x1_3y1_5r1_5x2_3y2_2(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_5r1_5x2_3y2_2["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_5r1_5x2_3y2_2["out"])

    def test_collision_x1_3y1_5r1_5x2_3y2_3r2_1(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_5r1_5x2_3y2_3r2_1["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_5r1_5x2_3y2_3r2_1["out"])

    def test_collision_x1_3y1_5r1_5x2_3y2_3r2_2(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_5r1_5x2_3y2_3r2_2["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_5r1_5x2_3y2_3r2_2["out"])

    def test_collision_x1_3y1_5r1_5x2_3y2_3r2_3(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_5r1_5x2_3y2_3r2_3["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_5r1_5x2_3y2_3r2_3["out"])

    def test_collision_x1_3y1_5r1_5x2_3y2_3r2_5(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_5r1_5x2_3y2_3r2_5["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_5r1_5x2_3y2_3r2_5["out"])

    def test_collision_x1_3y1_5r1_5x2_3y2_3r2_6(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_5r1_5x2_3y2_3r2_6["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_5r1_5x2_3y2_3r2_6["out"])

    def test_collision_x1_3y1_5r1_5x2_3y2_3r2_7(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_5r1_5x2_3y2_3r2_7["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_5r1_5x2_3y2_3r2_7["out"])

    def test_collision_x1_3y1_5r1_5x2_3y2_5r2_1(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_5r1_5x2_3y2_5r2_1["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_5r1_5x2_3y2_5r2_1["out"])

    def test_collision_x1_3y1_5r1_5x2_3y2_5r2_2(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_5r1_5x2_3y2_5r2_2["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_5r1_5x2_3y2_5r2_2["out"])

    def test_collision_x1_3y1_5r1_5x2_3y2_5r2_3(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_5r1_5x2_3y2_5r2_3["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_5r1_5x2_3y2_5r2_3["out"])

    def test_collision_x1_3y1_5r1_5x2_3y2_5r2_5(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_5r1_5x2_3y2_5r2_5["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_5r1_5x2_3y2_5r2_5["out"])

    def test_collision_x1_3y1_5r1_5x2_3y2_5r2_6(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_5r1_5x2_3y2_5r2_6["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_5r1_5x2_3y2_5r2_6["out"])

    def test_collision_x1_3y1_5r1_5x2_3y2_5r2_7(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_5r1_5x2_3y2_5r2_7["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_5r1_5x2_3y2_5r2_7["out"])

    def test_collision_x1_3y1_5r1_5x2_3y2_6(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_5r1_5x2_3y2_6["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_5r1_5x2_3y2_6["out"])

    def test_collision_x1_3y1_5r1_5x2_3y2_7(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_5r1_5x2_3y2_7["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_5r1_5x2_3y2_7["out"])

    def test_collision_x1_3y1_5r1_5x2_5y2_1(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_5r1_5x2_5y2_1["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_5r1_5x2_5y2_1["out"])

    def test_collision_x1_3y1_5r1_5x2_5y2_2(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_5r1_5x2_5y2_2["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_5r1_5x2_5y2_2["out"])

    def test_collision_x1_3y1_5r1_5x2_5y2_3r2_1(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_5r1_5x2_5y2_3r2_1["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_5r1_5x2_5y2_3r2_1["out"])

    def test_collision_x1_3y1_5r1_5x2_5y2_3r2_2(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_5r1_5x2_5y2_3r2_2["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_5r1_5x2_5y2_3r2_2["out"])

    def test_collision_x1_3y1_5r1_5x2_5y2_3r2_3(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_5r1_5x2_5y2_3r2_3["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_5r1_5x2_5y2_3r2_3["out"])

    def test_collision_x1_3y1_5r1_5x2_5y2_3r2_5(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_5r1_5x2_5y2_3r2_5["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_5r1_5x2_5y2_3r2_5["out"])

    def test_collision_x1_3y1_5r1_5x2_5y2_3r2_6(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_5r1_5x2_5y2_3r2_6["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_5r1_5x2_5y2_3r2_6["out"])

    def test_collision_x1_3y1_5r1_5x2_5y2_3r2_7(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_5r1_5x2_5y2_3r2_7["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_5r1_5x2_5y2_3r2_7["out"])

    def test_collision_x1_3y1_5r1_5x2_5y2_5r2_1(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_5r1_5x2_5y2_5r2_1["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_5r1_5x2_5y2_5r2_1["out"])

    def test_collision_x1_3y1_5r1_5x2_5y2_5r2_2(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_5r1_5x2_5y2_5r2_2["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_5r1_5x2_5y2_5r2_2["out"])

    def test_collision_x1_3y1_5r1_5x2_5y2_5r2_3(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_5r1_5x2_5y2_5r2_3["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_5r1_5x2_5y2_5r2_3["out"])

    def test_collision_x1_3y1_5r1_5x2_5y2_5r2_5(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_5r1_5x2_5y2_5r2_5["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_5r1_5x2_5y2_5r2_5["out"])

    def test_collision_x1_3y1_5r1_5x2_5y2_5r2_6(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_5r1_5x2_5y2_5r2_6["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_5r1_5x2_5y2_5r2_6["out"])

    def test_collision_x1_3y1_5r1_5x2_5y2_5r2_7(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_5r1_5x2_5y2_5r2_7["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_5r1_5x2_5y2_5r2_7["out"])

    def test_collision_x1_3y1_5r1_5x2_5y2_6(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_5r1_5x2_5y2_6["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_5r1_5x2_5y2_6["out"])

    def test_collision_x1_3y1_5r1_5x2_5y2_7(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_5r1_5x2_5y2_7["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_5r1_5x2_5y2_7["out"])

    def test_collision_x1_3y1_5r1_5x2_6(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_5r1_5x2_6["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_5r1_5x2_6["out"])

    def test_collision_x1_3y1_5r1_5x2_7(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_5r1_5x2_7["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_5r1_5x2_7["out"])

    def test_collision_x1_3y1_5r1_6(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_5r1_6["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_5r1_6["out"])

    def test_collision_x1_3y1_5r1_7(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_5r1_7["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_5r1_7["out"])

    def test_collision_x1_3y1_6(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_6["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_6["out"])

    def test_collision_x1_3y1_7(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_3y1_7["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_3y1_7["out"])

    def test_collision_x1_5y1_1(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_1["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_1["out"])

    def test_collision_x1_5y1_2(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_2["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_2["out"])

    def test_collision_x1_5y1_3r1_1(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_3r1_1["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_3r1_1["out"])

    def test_collision_x1_5y1_3r1_2(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_3r1_2["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_3r1_2["out"])

    def test_collision_x1_5y1_3r1_3x2_1(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_3r1_3x2_1["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_3r1_3x2_1["out"])

    def test_collision_x1_5y1_3r1_3x2_2(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_3r1_3x2_2["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_3r1_3x2_2["out"])

    def test_collision_x1_5y1_3r1_3x2_3y2_1(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_3r1_3x2_3y2_1["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_3r1_3x2_3y2_1["out"])

    def test_collision_x1_5y1_3r1_3x2_3y2_2(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_3r1_3x2_3y2_2["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_3r1_3x2_3y2_2["out"])

    def test_collision_x1_5y1_3r1_3x2_3y2_3r2_1(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_3r1_3x2_3y2_3r2_1["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_3r1_3x2_3y2_3r2_1["out"])

    def test_collision_x1_5y1_3r1_3x2_3y2_3r2_2(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_3r1_3x2_3y2_3r2_2["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_3r1_3x2_3y2_3r2_2["out"])

    def test_collision_x1_5y1_3r1_3x2_3y2_3r2_3(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_3r1_3x2_3y2_3r2_3["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_3r1_3x2_3y2_3r2_3["out"])

    def test_collision_x1_5y1_3r1_3x2_3y2_3r2_5(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_3r1_3x2_3y2_3r2_5["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_3r1_3x2_3y2_3r2_5["out"])

    def test_collision_x1_5y1_3r1_3x2_3y2_3r2_6(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_3r1_3x2_3y2_3r2_6["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_3r1_3x2_3y2_3r2_6["out"])

    def test_collision_x1_5y1_3r1_3x2_3y2_3r2_7(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_3r1_3x2_3y2_3r2_7["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_3r1_3x2_3y2_3r2_7["out"])

    def test_collision_x1_5y1_3r1_3x2_3y2_5r2_1(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_3r1_3x2_3y2_5r2_1["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_3r1_3x2_3y2_5r2_1["out"])

    def test_collision_x1_5y1_3r1_3x2_3y2_5r2_2(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_3r1_3x2_3y2_5r2_2["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_3r1_3x2_3y2_5r2_2["out"])

    def test_collision_x1_5y1_3r1_3x2_3y2_5r2_3(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_3r1_3x2_3y2_5r2_3["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_3r1_3x2_3y2_5r2_3["out"])

    def test_collision_x1_5y1_3r1_3x2_3y2_5r2_5(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_3r1_3x2_3y2_5r2_5["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_3r1_3x2_3y2_5r2_5["out"])

    def test_collision_x1_5y1_3r1_3x2_3y2_5r2_6(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_3r1_3x2_3y2_5r2_6["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_3r1_3x2_3y2_5r2_6["out"])

    def test_collision_x1_5y1_3r1_3x2_3y2_5r2_7(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_3r1_3x2_3y2_5r2_7["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_3r1_3x2_3y2_5r2_7["out"])

    def test_collision_x1_5y1_3r1_3x2_3y2_6(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_3r1_3x2_3y2_6["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_3r1_3x2_3y2_6["out"])

    def test_collision_x1_5y1_3r1_3x2_3y2_7(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_3r1_3x2_3y2_7["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_3r1_3x2_3y2_7["out"])

    def test_collision_x1_5y1_3r1_3x2_5y2_1(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_3r1_3x2_5y2_1["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_3r1_3x2_5y2_1["out"])

    def test_collision_x1_5y1_3r1_3x2_5y2_2(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_3r1_3x2_5y2_2["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_3r1_3x2_5y2_2["out"])

    def test_collision_x1_5y1_3r1_3x2_5y2_3r2_1(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_3r1_3x2_5y2_3r2_1["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_3r1_3x2_5y2_3r2_1["out"])

    def test_collision_x1_5y1_3r1_3x2_5y2_3r2_2(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_3r1_3x2_5y2_3r2_2["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_3r1_3x2_5y2_3r2_2["out"])

    def test_collision_x1_5y1_3r1_3x2_5y2_3r2_3(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_3r1_3x2_5y2_3r2_3["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_3r1_3x2_5y2_3r2_3["out"])

    def test_collision_x1_5y1_3r1_3x2_5y2_3r2_5(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_3r1_3x2_5y2_3r2_5["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_3r1_3x2_5y2_3r2_5["out"])

    def test_collision_x1_5y1_3r1_3x2_5y2_3r2_6(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_3r1_3x2_5y2_3r2_6["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_3r1_3x2_5y2_3r2_6["out"])

    def test_collision_x1_5y1_3r1_3x2_5y2_3r2_7(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_3r1_3x2_5y2_3r2_7["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_3r1_3x2_5y2_3r2_7["out"])

    def test_collision_x1_5y1_3r1_3x2_5y2_5r2_1(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_3r1_3x2_5y2_5r2_1["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_3r1_3x2_5y2_5r2_1["out"])

    def test_collision_x1_5y1_3r1_3x2_5y2_5r2_2(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_3r1_3x2_5y2_5r2_2["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_3r1_3x2_5y2_5r2_2["out"])

    def test_collision_x1_5y1_3r1_3x2_5y2_5r2_3(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_3r1_3x2_5y2_5r2_3["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_3r1_3x2_5y2_5r2_3["out"])

    def test_collision_x1_5y1_3r1_3x2_5y2_5r2_5(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_3r1_3x2_5y2_5r2_5["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_3r1_3x2_5y2_5r2_5["out"])

    def test_collision_x1_5y1_3r1_3x2_5y2_5r2_6(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_3r1_3x2_5y2_5r2_6["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_3r1_3x2_5y2_5r2_6["out"])

    def test_collision_x1_5y1_3r1_3x2_5y2_5r2_7(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_3r1_3x2_5y2_5r2_7["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_3r1_3x2_5y2_5r2_7["out"])

    def test_collision_x1_5y1_3r1_3x2_5y2_6(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_3r1_3x2_5y2_6["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_3r1_3x2_5y2_6["out"])

    def test_collision_x1_5y1_3r1_3x2_5y2_7(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_3r1_3x2_5y2_7["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_3r1_3x2_5y2_7["out"])

    def test_collision_x1_5y1_3r1_3x2_6(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_3r1_3x2_6["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_3r1_3x2_6["out"])

    def test_collision_x1_5y1_3r1_3x2_7(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_3r1_3x2_7["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_3r1_3x2_7["out"])

    def test_collision_x1_5y1_3r1_5x2_1(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_3r1_5x2_1["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_3r1_5x2_1["out"])

    def test_collision_x1_5y1_3r1_5x2_2(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_3r1_5x2_2["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_3r1_5x2_2["out"])

    def test_collision_x1_5y1_3r1_5x2_3y2_1(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_3r1_5x2_3y2_1["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_3r1_5x2_3y2_1["out"])

    def test_collision_x1_5y1_3r1_5x2_3y2_2(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_3r1_5x2_3y2_2["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_3r1_5x2_3y2_2["out"])

    def test_collision_x1_5y1_3r1_5x2_3y2_3r2_1(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_3r1_5x2_3y2_3r2_1["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_3r1_5x2_3y2_3r2_1["out"])

    def test_collision_x1_5y1_3r1_5x2_3y2_3r2_2(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_3r1_5x2_3y2_3r2_2["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_3r1_5x2_3y2_3r2_2["out"])

    def test_collision_x1_5y1_3r1_5x2_3y2_3r2_3(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_3r1_5x2_3y2_3r2_3["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_3r1_5x2_3y2_3r2_3["out"])

    def test_collision_x1_5y1_3r1_5x2_3y2_3r2_5(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_3r1_5x2_3y2_3r2_5["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_3r1_5x2_3y2_3r2_5["out"])

    def test_collision_x1_5y1_3r1_5x2_3y2_3r2_6(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_3r1_5x2_3y2_3r2_6["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_3r1_5x2_3y2_3r2_6["out"])

    def test_collision_x1_5y1_3r1_5x2_3y2_3r2_7(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_3r1_5x2_3y2_3r2_7["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_3r1_5x2_3y2_3r2_7["out"])

    def test_collision_x1_5y1_3r1_5x2_3y2_5r2_1(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_3r1_5x2_3y2_5r2_1["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_3r1_5x2_3y2_5r2_1["out"])

    def test_collision_x1_5y1_3r1_5x2_3y2_5r2_2(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_3r1_5x2_3y2_5r2_2["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_3r1_5x2_3y2_5r2_2["out"])

    def test_collision_x1_5y1_3r1_5x2_3y2_5r2_3(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_3r1_5x2_3y2_5r2_3["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_3r1_5x2_3y2_5r2_3["out"])

    def test_collision_x1_5y1_3r1_5x2_3y2_5r2_5(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_3r1_5x2_3y2_5r2_5["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_3r1_5x2_3y2_5r2_5["out"])

    def test_collision_x1_5y1_3r1_5x2_3y2_5r2_6(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_3r1_5x2_3y2_5r2_6["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_3r1_5x2_3y2_5r2_6["out"])

    def test_collision_x1_5y1_3r1_5x2_3y2_5r2_7(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_3r1_5x2_3y2_5r2_7["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_3r1_5x2_3y2_5r2_7["out"])

    def test_collision_x1_5y1_3r1_5x2_3y2_6(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_3r1_5x2_3y2_6["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_3r1_5x2_3y2_6["out"])

    def test_collision_x1_5y1_3r1_5x2_3y2_7(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_3r1_5x2_3y2_7["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_3r1_5x2_3y2_7["out"])

    def test_collision_x1_5y1_3r1_5x2_5y2_1(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_3r1_5x2_5y2_1["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_3r1_5x2_5y2_1["out"])

    def test_collision_x1_5y1_3r1_5x2_5y2_2(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_3r1_5x2_5y2_2["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_3r1_5x2_5y2_2["out"])

    def test_collision_x1_5y1_3r1_5x2_5y2_3r2_1(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_3r1_5x2_5y2_3r2_1["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_3r1_5x2_5y2_3r2_1["out"])

    def test_collision_x1_5y1_3r1_5x2_5y2_3r2_2(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_3r1_5x2_5y2_3r2_2["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_3r1_5x2_5y2_3r2_2["out"])

    def test_collision_x1_5y1_3r1_5x2_5y2_3r2_3(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_3r1_5x2_5y2_3r2_3["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_3r1_5x2_5y2_3r2_3["out"])

    def test_collision_x1_5y1_3r1_5x2_5y2_3r2_5(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_3r1_5x2_5y2_3r2_5["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_3r1_5x2_5y2_3r2_5["out"])

    def test_collision_x1_5y1_3r1_5x2_5y2_3r2_6(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_3r1_5x2_5y2_3r2_6["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_3r1_5x2_5y2_3r2_6["out"])

    def test_collision_x1_5y1_3r1_5x2_5y2_3r2_7(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_3r1_5x2_5y2_3r2_7["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_3r1_5x2_5y2_3r2_7["out"])

    def test_collision_x1_5y1_3r1_5x2_5y2_5r2_1(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_3r1_5x2_5y2_5r2_1["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_3r1_5x2_5y2_5r2_1["out"])

    def test_collision_x1_5y1_3r1_5x2_5y2_5r2_2(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_3r1_5x2_5y2_5r2_2["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_3r1_5x2_5y2_5r2_2["out"])

    def test_collision_x1_5y1_3r1_5x2_5y2_5r2_3(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_3r1_5x2_5y2_5r2_3["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_3r1_5x2_5y2_5r2_3["out"])

    def test_collision_x1_5y1_3r1_5x2_5y2_5r2_5(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_3r1_5x2_5y2_5r2_5["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_3r1_5x2_5y2_5r2_5["out"])

    def test_collision_x1_5y1_3r1_5x2_5y2_5r2_6(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_3r1_5x2_5y2_5r2_6["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_3r1_5x2_5y2_5r2_6["out"])

    def test_collision_x1_5y1_3r1_5x2_5y2_5r2_7(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_3r1_5x2_5y2_5r2_7["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_3r1_5x2_5y2_5r2_7["out"])

    def test_collision_x1_5y1_3r1_5x2_5y2_6(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_3r1_5x2_5y2_6["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_3r1_5x2_5y2_6["out"])

    def test_collision_x1_5y1_3r1_5x2_5y2_7(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_3r1_5x2_5y2_7["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_3r1_5x2_5y2_7["out"])

    def test_collision_x1_5y1_3r1_5x2_6(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_3r1_5x2_6["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_3r1_5x2_6["out"])

    def test_collision_x1_5y1_3r1_5x2_7(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_3r1_5x2_7["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_3r1_5x2_7["out"])

    def test_collision_x1_5y1_3r1_6(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_3r1_6["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_3r1_6["out"])

    def test_collision_x1_5y1_3r1_7(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_3r1_7["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_3r1_7["out"])

    def test_collision_x1_5y1_5r1_1(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_5r1_1["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_5r1_1["out"])

    def test_collision_x1_5y1_5r1_2(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_5r1_2["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_5r1_2["out"])

    def test_collision_x1_5y1_5r1_3x2_1(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_5r1_3x2_1["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_5r1_3x2_1["out"])

    def test_collision_x1_5y1_5r1_3x2_2(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_5r1_3x2_2["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_5r1_3x2_2["out"])

    def test_collision_x1_5y1_5r1_3x2_3y2_1(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_5r1_3x2_3y2_1["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_5r1_3x2_3y2_1["out"])

    def test_collision_x1_5y1_5r1_3x2_3y2_2(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_5r1_3x2_3y2_2["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_5r1_3x2_3y2_2["out"])

    def test_collision_x1_5y1_5r1_3x2_3y2_3r2_1(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_5r1_3x2_3y2_3r2_1["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_5r1_3x2_3y2_3r2_1["out"])

    def test_collision_x1_5y1_5r1_3x2_3y2_3r2_2(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_5r1_3x2_3y2_3r2_2["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_5r1_3x2_3y2_3r2_2["out"])

    def test_collision_x1_5y1_5r1_3x2_3y2_3r2_3(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_5r1_3x2_3y2_3r2_3["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_5r1_3x2_3y2_3r2_3["out"])

    def test_collision_x1_5y1_5r1_3x2_3y2_3r2_5(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_5r1_3x2_3y2_3r2_5["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_5r1_3x2_3y2_3r2_5["out"])

    def test_collision_x1_5y1_5r1_3x2_3y2_3r2_6(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_5r1_3x2_3y2_3r2_6["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_5r1_3x2_3y2_3r2_6["out"])

    def test_collision_x1_5y1_5r1_3x2_3y2_3r2_7(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_5r1_3x2_3y2_3r2_7["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_5r1_3x2_3y2_3r2_7["out"])

    def test_collision_x1_5y1_5r1_3x2_3y2_5r2_1(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_5r1_3x2_3y2_5r2_1["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_5r1_3x2_3y2_5r2_1["out"])

    def test_collision_x1_5y1_5r1_3x2_3y2_5r2_2(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_5r1_3x2_3y2_5r2_2["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_5r1_3x2_3y2_5r2_2["out"])

    def test_collision_x1_5y1_5r1_3x2_3y2_5r2_3(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_5r1_3x2_3y2_5r2_3["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_5r1_3x2_3y2_5r2_3["out"])

    def test_collision_x1_5y1_5r1_3x2_3y2_5r2_5(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_5r1_3x2_3y2_5r2_5["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_5r1_3x2_3y2_5r2_5["out"])

    def test_collision_x1_5y1_5r1_3x2_3y2_5r2_6(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_5r1_3x2_3y2_5r2_6["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_5r1_3x2_3y2_5r2_6["out"])

    def test_collision_x1_5y1_5r1_3x2_3y2_5r2_7(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_5r1_3x2_3y2_5r2_7["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_5r1_3x2_3y2_5r2_7["out"])

    def test_collision_x1_5y1_5r1_3x2_3y2_6(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_5r1_3x2_3y2_6["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_5r1_3x2_3y2_6["out"])

    def test_collision_x1_5y1_5r1_3x2_3y2_7(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_5r1_3x2_3y2_7["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_5r1_3x2_3y2_7["out"])

    def test_collision_x1_5y1_5r1_3x2_5y2_1(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_5r1_3x2_5y2_1["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_5r1_3x2_5y2_1["out"])

    def test_collision_x1_5y1_5r1_3x2_5y2_2(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_5r1_3x2_5y2_2["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_5r1_3x2_5y2_2["out"])

    def test_collision_x1_5y1_5r1_3x2_5y2_3r2_1(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_5r1_3x2_5y2_3r2_1["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_5r1_3x2_5y2_3r2_1["out"])

    def test_collision_x1_5y1_5r1_3x2_5y2_3r2_2(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_5r1_3x2_5y2_3r2_2["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_5r1_3x2_5y2_3r2_2["out"])

    def test_collision_x1_5y1_5r1_3x2_5y2_3r2_3(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_5r1_3x2_5y2_3r2_3["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_5r1_3x2_5y2_3r2_3["out"])

    def test_collision_x1_5y1_5r1_3x2_5y2_3r2_5(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_5r1_3x2_5y2_3r2_5["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_5r1_3x2_5y2_3r2_5["out"])

    def test_collision_x1_5y1_5r1_3x2_5y2_3r2_6(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_5r1_3x2_5y2_3r2_6["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_5r1_3x2_5y2_3r2_6["out"])

    def test_collision_x1_5y1_5r1_3x2_5y2_3r2_7(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_5r1_3x2_5y2_3r2_7["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_5r1_3x2_5y2_3r2_7["out"])

    def test_collision_x1_5y1_5r1_3x2_5y2_5r2_1(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_5r1_3x2_5y2_5r2_1["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_5r1_3x2_5y2_5r2_1["out"])

    def test_collision_x1_5y1_5r1_3x2_5y2_5r2_2(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_5r1_3x2_5y2_5r2_2["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_5r1_3x2_5y2_5r2_2["out"])

    def test_collision_x1_5y1_5r1_3x2_5y2_5r2_3(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_5r1_3x2_5y2_5r2_3["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_5r1_3x2_5y2_5r2_3["out"])

    def test_collision_x1_5y1_5r1_3x2_5y2_5r2_5(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_5r1_3x2_5y2_5r2_5["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_5r1_3x2_5y2_5r2_5["out"])

    def test_collision_x1_5y1_5r1_3x2_5y2_5r2_6(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_5r1_3x2_5y2_5r2_6["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_5r1_3x2_5y2_5r2_6["out"])

    def test_collision_x1_5y1_5r1_3x2_5y2_5r2_7(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_5r1_3x2_5y2_5r2_7["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_5r1_3x2_5y2_5r2_7["out"])

    def test_collision_x1_5y1_5r1_3x2_5y2_6(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_5r1_3x2_5y2_6["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_5r1_3x2_5y2_6["out"])

    def test_collision_x1_5y1_5r1_3x2_5y2_7(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_5r1_3x2_5y2_7["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_5r1_3x2_5y2_7["out"])

    def test_collision_x1_5y1_5r1_3x2_6(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_5r1_3x2_6["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_5r1_3x2_6["out"])

    def test_collision_x1_5y1_5r1_3x2_7(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_5r1_3x2_7["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_5r1_3x2_7["out"])

    def test_collision_x1_5y1_5r1_5x2_1(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_5r1_5x2_1["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_5r1_5x2_1["out"])

    def test_collision_x1_5y1_5r1_5x2_2(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_5r1_5x2_2["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_5r1_5x2_2["out"])

    def test_collision_x1_5y1_5r1_5x2_3y2_1(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_5r1_5x2_3y2_1["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_5r1_5x2_3y2_1["out"])

    def test_collision_x1_5y1_5r1_5x2_3y2_2(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_5r1_5x2_3y2_2["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_5r1_5x2_3y2_2["out"])

    def test_collision_x1_5y1_5r1_5x2_3y2_3r2_1(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_5r1_5x2_3y2_3r2_1["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_5r1_5x2_3y2_3r2_1["out"])

    def test_collision_x1_5y1_5r1_5x2_3y2_3r2_2(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_5r1_5x2_3y2_3r2_2["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_5r1_5x2_3y2_3r2_2["out"])

    def test_collision_x1_5y1_5r1_5x2_3y2_3r2_3(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_5r1_5x2_3y2_3r2_3["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_5r1_5x2_3y2_3r2_3["out"])

    def test_collision_x1_5y1_5r1_5x2_3y2_3r2_5(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_5r1_5x2_3y2_3r2_5["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_5r1_5x2_3y2_3r2_5["out"])

    def test_collision_x1_5y1_5r1_5x2_3y2_3r2_6(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_5r1_5x2_3y2_3r2_6["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_5r1_5x2_3y2_3r2_6["out"])

    def test_collision_x1_5y1_5r1_5x2_3y2_3r2_7(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_5r1_5x2_3y2_3r2_7["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_5r1_5x2_3y2_3r2_7["out"])

    def test_collision_x1_5y1_5r1_5x2_3y2_5r2_1(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_5r1_5x2_3y2_5r2_1["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_5r1_5x2_3y2_5r2_1["out"])

    def test_collision_x1_5y1_5r1_5x2_3y2_5r2_2(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_5r1_5x2_3y2_5r2_2["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_5r1_5x2_3y2_5r2_2["out"])

    def test_collision_x1_5y1_5r1_5x2_3y2_5r2_3(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_5r1_5x2_3y2_5r2_3["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_5r1_5x2_3y2_5r2_3["out"])

    def test_collision_x1_5y1_5r1_5x2_3y2_5r2_5(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_5r1_5x2_3y2_5r2_5["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_5r1_5x2_3y2_5r2_5["out"])

    def test_collision_x1_5y1_5r1_5x2_3y2_5r2_6(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_5r1_5x2_3y2_5r2_6["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_5r1_5x2_3y2_5r2_6["out"])

    def test_collision_x1_5y1_5r1_5x2_3y2_5r2_7(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_5r1_5x2_3y2_5r2_7["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_5r1_5x2_3y2_5r2_7["out"])

    def test_collision_x1_5y1_5r1_5x2_3y2_6(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_5r1_5x2_3y2_6["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_5r1_5x2_3y2_6["out"])

    def test_collision_x1_5y1_5r1_5x2_3y2_7(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_5r1_5x2_3y2_7["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_5r1_5x2_3y2_7["out"])

    def test_collision_x1_5y1_5r1_5x2_5y2_1(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_5r1_5x2_5y2_1["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_5r1_5x2_5y2_1["out"])

    def test_collision_x1_5y1_5r1_5x2_5y2_2(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_5r1_5x2_5y2_2["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_5r1_5x2_5y2_2["out"])

    def test_collision_x1_5y1_5r1_5x2_5y2_3r2_1(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_5r1_5x2_5y2_3r2_1["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_5r1_5x2_5y2_3r2_1["out"])

    def test_collision_x1_5y1_5r1_5x2_5y2_3r2_2(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_5r1_5x2_5y2_3r2_2["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_5r1_5x2_5y2_3r2_2["out"])

    def test_collision_x1_5y1_5r1_5x2_5y2_3r2_3(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_5r1_5x2_5y2_3r2_3["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_5r1_5x2_5y2_3r2_3["out"])

    def test_collision_x1_5y1_5r1_5x2_5y2_3r2_5(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_5r1_5x2_5y2_3r2_5["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_5r1_5x2_5y2_3r2_5["out"])

    def test_collision_x1_5y1_5r1_5x2_5y2_3r2_6(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_5r1_5x2_5y2_3r2_6["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_5r1_5x2_5y2_3r2_6["out"])

    def test_collision_x1_5y1_5r1_5x2_5y2_3r2_7(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_5r1_5x2_5y2_3r2_7["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_5r1_5x2_5y2_3r2_7["out"])

    def test_collision_x1_5y1_5r1_5x2_5y2_5r2_1(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_5r1_5x2_5y2_5r2_1["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_5r1_5x2_5y2_5r2_1["out"])

    def test_collision_x1_5y1_5r1_5x2_5y2_5r2_2(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_5r1_5x2_5y2_5r2_2["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_5r1_5x2_5y2_5r2_2["out"])

    def test_collision_x1_5y1_5r1_5x2_5y2_5r2_3(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_5r1_5x2_5y2_5r2_3["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_5r1_5x2_5y2_5r2_3["out"])

    def test_collision_x1_5y1_5r1_5x2_5y2_5r2_5(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_5r1_5x2_5y2_5r2_5["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_5r1_5x2_5y2_5r2_5["out"])

    def test_collision_x1_5y1_5r1_5x2_5y2_5r2_6(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_5r1_5x2_5y2_5r2_6["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_5r1_5x2_5y2_5r2_6["out"])

    def test_collision_x1_5y1_5r1_5x2_5y2_5r2_7(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_5r1_5x2_5y2_5r2_7["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_5r1_5x2_5y2_5r2_7["out"])

    def test_collision_x1_5y1_5r1_5x2_5y2_6(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_5r1_5x2_5y2_6["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_5r1_5x2_5y2_6["out"])

    def test_collision_x1_5y1_5r1_5x2_5y2_7(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_5r1_5x2_5y2_7["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_5r1_5x2_5y2_7["out"])

    def test_collision_x1_5y1_5r1_5x2_6(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_5r1_5x2_6["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_5r1_5x2_6["out"])

    def test_collision_x1_5y1_5r1_5x2_7(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_5r1_5x2_7["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_5r1_5x2_7["out"])

    def test_collision_x1_5y1_5r1_6(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_5r1_6["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_5r1_6["out"])

    def test_collision_x1_5y1_5r1_7(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_5r1_7["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_5r1_7["out"])

    def test_collision_x1_5y1_6(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_6["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_6["out"])

    def test_collision_x1_5y1_7(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_5y1_7["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_5y1_7["out"])

    def test_collision_x1_6(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_6["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_6["out"])

    def test_collision_x1_7(self):
        x1, y1, r1, x2, y2, r2 = collision_x1_7["in"]
        result = main(x1, y1, r1, x2, y2, r2)
        self.assertEqual(result, collision_x1_7["out"])

if __name__ == '__main__':
    unittest.main()