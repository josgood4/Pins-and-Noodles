from Noodles import *

class Board():

  def __init__(self, pinList, size, noodleList):
    self.__pinList = pinList
    self.__size = size
    self.__noodleList = noodleList

  def isPin(self, nood, coord):
    for eachPin in self.__pinList:
      if coord[0] == eachPin[0] and coord[1] == eachPin[1] and \
          nood.getPinLoc()[0] != eachPin[0] and nood.getPinLoc()[1] != eachPin[1]
        return True
    return False

  def isNotInBounds(self, coord):
    return coord[0]<0 or coord[1]<0 or coord[0]>=self.__size or coord[1]>=self.__size

  #TODO: TEST ME!!!!!
  # checks if coord collides with nood
  # (assumes nood IS placed)
  # NOTE: MAKE SURE nood != the current coord
  def collidesWithPiece(self, nood, coord):
    for eachCoord in nood.getCurrentShape():
      if eachCoord[0]==coord[0] and eachCoord[1]==coord[1]:
        return True
    return False

  #TODO: TEST ME!!!!!
  def checkPiece(self, currentN):
    for eachN in noodleList:
      # let's hope this second bool expression is sufficient...
      if eachN.isPiecePlaced() and eachN != currentN:
        for eachCoord in currentN.getCurrentShape():
          if self.collidesWithPiece(eachN, coord) or self.isPin(currentN, coord) \
               or self.isNotInBounds(coord):
            return True
    return False
        
        
