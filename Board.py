from Noodles import *

class Board():

  def __init__(self, pinList, size, noodleList):
    self.__pinList = pinList
    self.__size = size
    self.__noodleList = noodleList
    self.__boolGrid = []
    for i in range(size):
      self.__boolGrid.append([False] * size)

  def getBools(self):
    return self.__boolGrid

  def isPin(self, nood, coord):
    for eachPin in self.__pinList:
      if coord[0] == eachPin[0] and coord[1] == eachPin[1] and \
                    not(nood.isOwnNode(coord)):
        return True
    return False

  def isNotInBounds(self, coord):
    return coord[0]<0 or coord[1]<0 or coord[0]>=self.__size or coord[1]>=self.__size

        
  def tryToPlacePiece(self, nood, pinNum, orient):
    nood.placePiece(self.__pinList[pinNum], orient)
    for eachCoord in nood.getCurrentSquares():
      print("checking %d, %d... " % (eachCoord[0], eachCoord[1]))
      if self.isNotInBounds(eachCoord) or \
            self.__boolGrid[eachCoord[1]][eachCoord[0]] or \
            self.isPin(nood, eachCoord):
        print("\tUH OH!")
        print("\tnot in bounds? %s, boolGrid? %s, is pin? %s" %\
              (self.isNotInBounds(eachCoord), \
               self.__boolGrid[eachCoord[1]][eachCoord[0]], \
               self.isPin(nood, eachCoord)))
        self.unplacePiece(nood, pinNum, orient)
        return None
      else: 
        print("\tgoooood...")
        self.__boolGrid[eachCoord[1]][eachCoord[0]] = True 
        
  def unplacePiece(self, nood, pinNum, orient):
    for eachCoord in nood.getSomeSquares(self.__pinList[pinNum], orient):
      if not(self.isNotInBounds(eachCoord)):
        self.__boolGrid[eachCoord[1]][eachCoord[0]] = False
    nood.unplacePiece()

  def __isPinJustCoordCheck(self, coord):
    for eachPin in self.__pinList:
      if coord[0] == eachPin[0] and coord[1] == eachPin[1]:
        return True
    return False

  def __str__(self):
    retStr = ""
    for y in range(self.__size):
      for x in range(self.__size):
        if self.__isPinJustCoordCheck((x,y)):
          retStr += "o\t"
        elif self.__boolGrid[y][x]:
          retStr += "X\t"
        else:
          retStr += "_\t"
      retStr += "\n"
    return retStr

  """
  #TODO: TEST ME!!!!!
  # checks if coord collides with nood
  # (assumes nood IS placed)
  # NOTE: MAKE SURE nood != the current coord
  def collidesWithPiece(self, nood, coord):
    for eachCoord in nood.getCurrentSquares():
      if eachCoord[0]==coord[0] and eachCoord[1]==coord[1]:
        return True
    return False
  """

  """
  #TODO: TEST ME!!!!!
  def checkPiece(self, currentN):
    for eachN in noodleList:
      # let's hope this second bool expression is sufficient...
      if eachN.isPiecePlaced() and eachN != currentN:
        for eachCoord in currentN.getCurrentSquares():
          if self.collidesWithPiece(eachN, eachCoord) or self.isPin(currentN, eachCoord) \
               or self.isNotInBounds(eachCoord):
            return True
    return False
  """
