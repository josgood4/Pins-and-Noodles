from Noodles import *
from Board import *
import numpy as np

tempM = np.matrix([[0,0],[0,1],[0,2],[1,2],[2,2]])
print(tempM)

n1 = Noodle(tempM, False)
print(n1.getPiecePossibilities())

