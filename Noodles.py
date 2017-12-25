import numpy as np

class Noodle():

  rotM = np.matrix([[0,1] , [-1,0]])
  reflM = np.matrix([[-1,0] , [0,1]])
  
  # pieceShape is defined as 2D array, of shape
  #   [ [x1, y1] , [x2, y2] , ... , [xn, yn] ] 
  #   each [xi, yi] representing the positions 
  #   relative to [0,0] that the piece covers up
  # NOTE: [0,0] is always pinPos
  def __init__(self, pieceShape, isSym):
    self.__pieceShape = pieceShape #2D array, see above
    self.__isSym = isSym #bool

  # return a list of different piece orientations
  def getPiecePossibilities(self):
    retL = []
    tempM = self.__pieceShape
    for i in range(4):
      retL.append(tempM)
      tempM = tempM * Noodle.rotM
    if self.__isSym:
      return retL

    tempM = tempM * Noodle.reflM
    for i in range(4):
      retL.append(tempM)
      tempM = tempM * Noodle.rotM
    return retL
