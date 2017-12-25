from Noodles import *

class Board():

  def __init__(self, pinList, size, noodleList):
    self.__pinList = pinList
    self.__size = size
    self.__noodleList = noodleList

  def isPin(self, coord):
    for eachPin in self.__pinList:
      if coord[0] == eachPin[0] and coord[1] == eachPin[1]:
        return True
    return False

  def isInBounds(self, coord):
    return coord[0]>=0 and coord[1]>=0 and coord[0]<self.__size and coord[1]<self.__size

  # assumes nood is already placed
  def collidesWithPiece(self, nood, coord):
    for eachCoord in nood.getCurrentShape():


  def hasCollisions(self, nood):
    for eachN in noodleList:
      if eachN.isPiecePlaced():
        
        
