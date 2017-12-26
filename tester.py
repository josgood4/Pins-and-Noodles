from Noodles import *
from Board import *
import numpy as np

myL = [0,1,2,3,4,5]

"""
bn = Board([[]], 0)
print(bn.getSmallerList(myL, 0))
print(bn.getSmallerList(myL, 1))
print(bn.getSmallerList(myL, 3))
print(bn.getSmallerList(myL, 5))
"""

t1 = np.matrix([[0,0],[0,1],[0,2],[1,2],[2,2]])
##print(t1)
n1 = Noodle("n1", t1, False)
##print(n1.getPiecePossibilities())

t2 = np.matrix([[0,0],[0,1],[1,0],[1,1]])
n2 = Noodle("n2", t2, True)

b1 = Board([[0,0], [1,1]], 3, [n1, n2])
print(b1)

print(b1.checkAll())

"""
b1.tryToPlacePiece(n1, 0, 0)
print(b1)

for i in range(4):
  b1.tryToPlacePiece(n2, 1, i)
  print(b1)
  b1.unplacePiece(n2, 1, i)

b1.unplacePiece(n1, 0, 0)
b1.unplacePiece(n2, 1, 3)
print(b1)

print("orientations:")
for i in range(8):
  b1.tryToPlacePiece(n1, 0, i)
  print(b1)
  b1.unplacePiece(n1, 0, i)
  ##print(n1.getCurrentSquares())
  ##for coord in n1.getCurrentSquares():
    ##if b1.isNotInBounds(coord):
      ##print("%d, %d is NOT in bounds" % (coord[0], coord[1]))
    ##else: 
      ##print("%d, %d IS in bounds" % (coord[0], coord[1]))
"""

