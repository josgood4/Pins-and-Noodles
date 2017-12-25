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
    self.__currentOrient = -1 #int ranging from 0 to 8
    self.__orients = self.getPiecePossibilities()
    self.__pinLoc = None

  def getSym(self):
    return self.__isSym

  # return a list of different piece orientations
  def getPiecePossibilities(self):
    retL = []
    tempM = self.__pieceShape
    for i in range(4):
      retL.append(np.ndarray.tolist(tempM))
      tempM = tempM * Noodle.rotM
    if self.__isSym:
      return retL

    tempM = tempM * Noodle.reflM
    for i in range(4):
      retL.append(np.ndarray.tolist(tempM))
      tempM = tempM * Noodle.rotM
    return retL

  def getPinLoc(self):
    return self.__pinLoc

  def getCurrentOrient(self):
    return self.__currentOrient

  def placePiece(self, pinLoc, orientation):
    self.__pinLoc = pinLoc
    self.__currentOrient = orientation

  def unplacePiece(self):
    self.__pinLoc = None
    self.__currentOrient = -1

  def isPlaced(self):
    return bool(self.__pinLoc)

  def isOwnNode(self, coord):
    return self.__pinLoc[0] == coord[0] and self.__pinLoc[1] == coord[1]

  def getCurrentSquares(self):
    if bool(self.__pinLoc) == False:
      return None
    retList = []
    for eachCoord in self.__orients[self.__currentOrient]:
      retList.append([eachCoord[0]+self.__pinLoc[0], \
                      eachCoord[1]+self.__pinLoc[1]])
    return retList

  def getSomeSquares(self, pinLoc, orient):
    retList = []
    for eachCoord in self.__orients[orient]:
      retList.append([eachCoord[0]+pinLoc[0], \
                      eachCoord[1]+pinLoc[1]])
    return retList
