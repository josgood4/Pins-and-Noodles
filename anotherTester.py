from Noodles import *
from Board import *
import numpy as np

t1 = np.matrix([[0,0],[0,-1],[0,-2],[1,-2],[2,-2]])
n1 = Noodle(t1, False)

t2 = np.matrix([[0,0],[-1,0],[-1,1],[-1,2], [-2,2]])
n2 = Noodle(t2, False)

t3 = np.matrix([[0,0],[0,-1],[1,-1],[1,-2],[2,-1]])
n3 = Noodle(t3, False)

holes = [[0,4],[1,4],[2,4],[3,4],[4,4],[3,3],[4,3],[3,0],[4,0],[4,1]]

b1 = Board([[0,2], [2,1], [2,3]], 5, [n1, n2, n3], holes)
print(b1)

print(b1.checkAll())
