from Noodles import *
from Board import *
import numpy as np

tempM = np.matrix([[0,0],[0,1],[0,2],[1,2],[2,2]])
print(tempM)

n1 = Noodle(tempM, False)
b1 = Board([[0,0]], 3, [n1])

print(n1.getPiecePossibilities())

print("orientations:")
for i in range(8):
  n1.placePiece([0,0], i)
  print(n1.getCurrentSquares())
  #TODO: TEST collidesWithPiece, isPin 
  for coord in n1.getCurrentSquares():
    if b1.isNotInBounds(coord):
      print("%d, %d is NOT in bounds" % (coord[0], coord[1]))
    else: 
      print("%d, %d IS in bounds" % (coord[0], coord[1]))
