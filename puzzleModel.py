from Noodles import *
from Board import *
import numpy as np
import timeit

n01 = Noodle("n01", np.matrix([(0,0), (0,-1), (0,-2), (1,-2), (2,-2) ]), False)
n02 = Noodle("n02", np.matrix([(0,0), (-1,0), (-1,1), (-1,2), (-2,2) ]), False)
n03 = Noodle("n03", np.matrix([(0,0), (0,-1), (1,-1), (2,-1), (1,-2) ]), False)
n04 = Noodle("n04", np.matrix([(0,0), (-1,0), (-2,0), (-3,0), (-2,1) ]), False)
n05 = Noodle("n05", np.matrix([(0,0), (0,1),  (0,2),  (-1,1), (-2,1) ]), False)
n06 = Noodle("n06", np.matrix([(0,0), (-1,0), (-2,0), (-1,-1),(-2,-1)]), False)
n07 = Noodle("n07", np.matrix([(0,0), (1,0),  (0,1),  (0,2),  (1,2)  ]), False)
n08 = Noodle("n08", np.matrix([(0,0), (-1,0), (-2,0), (-1,-1),(-1,1) ]), True )
n09 = Noodle("n09", np.matrix([(0,0), (0,1),  (-1,1), (-1,2), (-2,-2)]), False)
n10 = Noodle("n10", np.matrix([(0,0), (0,-1), (1,-1), (1,-2), (1,-3) ]), False)
n11 = Noodle("n11", np.matrix([(0,0), (0,1),  (0,2),  (0,3),  (-1,3) ]), False)
n12 = Noodle("n12", np.matrix([(0,0), (1,0),  (2,0),  (3,0),  (4,0)  ]), True )

noods = [n12,n01,n02,n03,n04,n05,n06,n07,n08,n09,n10,n11]

holes = [(3,3),(3,4),(4,3),(4,4)]

pins = [(6,0),(7,0),(2,1),(0,2),(2,3),(7,3),(0,4),(5,4),(7,4),(3,5),(0,7),(5,7)]

b1 = Board(pins, 8, noods, holes)

b1.printNumPossPlaces()
b1.sortByNumPlaces()
b1.printNumPossPlaces()

"""
start = timeit.default_timer()
print(b1.checkAll())
stop = timeit.default_timer()

print(stop - start)
"""
