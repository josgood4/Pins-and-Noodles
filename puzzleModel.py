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
n09 = Noodle("n09", np.matrix([(0,0), (0,1),  (-1,1), (-1,2), (-2,2) ]), False)
n10 = Noodle("n10", np.matrix([(0,0), (0,-1), (1,-1), (1,-2), (1,-3) ]), False)
n11 = Noodle("n11", np.matrix([(0,0), (0,1),  (0,2),  (0,3),  (-1,3) ]), False)
n12 = Noodle("n12", np.matrix([(0,0), (1,0),  (2,0),  (3,0),  (4,0)  ]), True )

noods = [n01,n02,n03,n04,n05,n06,n07,n08,n09,n10,n11,n12]

holes = [(3,3),(3,4),(4,3),(4,4)]

pins = [(6,0),(7,0),(2,1),(0,2),(2,3),(7,3),(0,4),(5,4),(7,4),(3,5),(0,7),(5,7)]

b1 = Board(pins, 8, noods, holes)

##print(b1)

"""
#known solution:
b1.tryToPlacePiece(n01, 3, 0)
b1.tryToPlacePiece(n02, 2, 0)
b1.tryToPlacePiece(n03, 4, 0)
b1.tryToPlacePiece(n04, 0, 0)
b1.tryToPlacePiece(n05, 1, 0)
b1.tryToPlacePiece(n06, 5, 0)
b1.tryToPlacePiece(n07, 6, 0)
b1.tryToPlacePiece(n08, 9, 0)
b1.tryToPlacePiece(n09, 7, 0)
b1.tryToPlacePiece(n10, 11, 0)
b1.tryToPlacePiece(n11, 8, 0)
b1.tryToPlacePiece(n12, 10, 0)

print(b1)

b1 = Board(pins, 8, noods, holes)
"""

##b1.printPossPlaces()

start = timeit.default_timer()
print(b1.checkAll())
stop = timeit.default_timer()

runTime = stop - start
numIters = b1.getIterProgress()

print("run time: %d" % runTime)
print("number of iterations: %d" % numIters)
print("iterations/second: %d" % (numIters/runTime))
