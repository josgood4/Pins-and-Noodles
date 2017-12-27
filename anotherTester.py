from Noodles import *
from Board import *
import numpy as np
import timeit

t1 = np.matrix([[0,0],[0,-1],[0,-2],[1,-2],[2,-2]])
n1 = Noodle("n1", t1, False)

t2 = np.matrix([[0,0],[-1,0],[-1,1],[-1,2], [-2,2]])
n2 = Noodle("n2", t2, False)

t3 = np.matrix([[0,0],[0,-1],[1,-1],[1,-2],[2,-1]])
n3 = Noodle("n3", t3, False)

holes = [[0,4],[1,4],[2,4],[3,4],[4,4],[3,3],[4,3],[3,0],[4,0],[4,1]]

b1 = Board([[0,2], [2,1], [2,3]], 5, [n1, n2, n3], holes)
print(b1)

start = timeit.default_timer()
print(b1.checkAll())
stop = timeit.default_timer()

runTime = stop - start
numIters = b1.getNumIters()
print("iterations/second: %d" % (numIters/runTime))

########################################################################

no1 = Noodle("no1", np.matrix([(0,0),(0,1),(0,2),(1,0),(2,0)]), True)
no2 = Noodle("no2", np.matrix([(0,0),(0,-1),(1,0),(1,-1),(2,0),(2,-1)]), False)
no3 = Noodle("no3", np.matrix([(0,0),(-1,0),(-2,0),(-3,0)]), True)
no4 = Noodle("no4", np.matrix([(0,0),(1,0),(0,1),(1,1),(0,2)]), False)
no5 = Noodle("no5", np.matrix([(0,0),(-1,0),(0,-1)]), True)

holes2 = [(3,0)]
for i in range(6):
  holes2.append((i,4))
  holes2.append((i,5))

b2 = Board([(0,0),(1,2),(3,3),(4,0),(5,3)], 6, [no1,no2,no3,no4,no5], holes2)

##b2.printPossPlaces()
##for eachNood in b2.getNoodleList():
  ##print("%s: %d" % (eachNood.getName(), eachNood.numPossPlaces))

start = timeit.default_timer()
##print(b2.checkAll())
stop = timeit.default_timer()

runTime = stop - start
numIters = b2.getNumIters()
##print(runTime)
##print(numIters)
print("iterations/second: %d" % (numIters/runTime))
