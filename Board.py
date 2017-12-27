from Noodles import *

BAR_SIZE = 50

class Board():

  def __init__(self, pinList, size, noodleList=None, holeList=None):
    self.__pinList = pinList
    self.__size = size
    self.__noodleList = [] if noodleList==None else noodleList
    self.__boolGrid = []
    for i in range(size):
      self.__boolGrid.append([False] * size)
    self.__holeList = [] if holeList==None else holeList 
    self.__solutionSet = []
    self.__numIters = 1

  def getBools(self):
    return self.__boolGrid

  def getNoodleList(self):
    return self.__noodleList

  def getIterProgress(self):
    return self.__iterProgress

#####################################################################
############################   BOOLS   ##############################
#####################################################################

  def isPin(self, nood, coord):
    for eachPin in self.__pinList:
      if coord[0] == eachPin[0] and coord[1] == eachPin[1] and \
                    not(nood.isOwnNode(coord)):
        return True
    return False

  def isNotInBounds(self, coord):
    retBool = False
    if coord[0]<0 or coord[1]<0 or coord[0]>=self.__size or coord[1]>=self.__size:
      retBool = True
    if self.__holeList!=None:
      for eachCoord in self.__holeList:
        if coord[0]==eachCoord[0] and coord[1]==eachCoord[1]:
          retBool = True
    return retBool

  def __isPinJustCoordCheck(self, coord):
    for eachPin in self.__pinList:
      if coord[0] == eachPin[0] and coord[1] == eachPin[1]:
        return True
    return False

  def __isHole(self, coord):
    if self.__holeList == None:
      return False
    for eachCoord in self.__holeList:
      if coord[0] == eachCoord[0] and coord[1] == eachCoord[1]:
        return True
    return False

#####################################################################
############################   LOGIC   ##############################
#####################################################################

                           #############
                           #(UN)PLACING#
                           #############

  def tryToPlacePiece(self, nood, pinNum, orient):
    nood.placePiece(self.__pinList[pinNum], orient)
    for eachCoord in nood.getCurrentSquares():
      ##print("checking %d, %d... " % (eachCoord[0], eachCoord[1]))
      if self.isNotInBounds(eachCoord) or \
            self.__boolGrid[eachCoord[1]][eachCoord[0]] or \
            self.isPin(nood, eachCoord):
        ##print("\tUH OH!")
        ##print("\tnot in bounds? %s, boolGrid? %s, is pin? %s" %\
              ##(self.isNotInBounds(eachCoord), \
               ##self.__boolGrid[eachCoord[1]][eachCoord[0]], \
               ##self.isPin(nood, eachCoord)))
        self.unplacePieceUpTo(nood, pinNum, orient, eachCoord)
        return None
      else: 
        ##print("\tgoooood...")
        self.__boolGrid[eachCoord[1]][eachCoord[0]] = True 
    return (nood, self.__pinList[pinNum], orient)
        
  def unplacePieceUpTo(self, nood, pinNum, orient, currentCoord):
    tempList = nood.getSomeSquares(self.__pinList[pinNum], orient)
    i = 0
    while tempList[i] != currentCoord and i<len(tempList):
      eachCoord = tempList[i]
      ##print("cleaning up: %d, %d" % (eachCoord[0], eachCoord[1]))
      if not(self.isNotInBounds(eachCoord)):
        self.__boolGrid[eachCoord[1]][eachCoord[0]] = False
      i += 1
    nood.unplacePiece()

  def unplacePiece(self, nood, pinNum, orient):
    for eachCoord in nood.getSomeSquares(self.__pinList[pinNum], orient):
      if not(self.isNotInBounds(eachCoord)):
        self.__boolGrid[eachCoord[1]][eachCoord[0]] = False
    nood.unplacePiece()

                      ##########################
                      # CHECKING POSSIBILITIES #
                      ##########################

  def __allPlaced(self):
    for y in range(self.__size):
      for x in range(self.__size):
        if not(self.__boolGrid[y][x]) and \
           not(self.__isHole((x,y))):
          return False
    return True
    """
    retBool = True
    for eachNood in self.__noodleList:
      print("\t\t\t\tis placed? %s" % eachNood.isPlaced())
      retBool = retBool and eachNood.isPlaced()
    return retBool
    """

  def __getSmallerList(self, list, idxToRmv):
    return list[:idxToRmv] + list[idxToRmv+1:]

  def __checkAllHelper(self, noodleList):
    result = []
    # base case
    if len(noodleList)==0:
      print("base case!")
      for eachNood in self.__noodleList:
        result.append((eachNood.getName(), eachNood.getPinLoc(), eachNood.getCurrentOrient()))
      result.append(None)
      return result
    # recursive case
    eachNood = noodleList[0]
    for (pinNum,eachOrient) in eachNood.possPlacements:
      if not(self.isPinOccupied(pinNum)):
        self.__iterProgress += 1
        didPlace = self.tryToPlacePiece(eachNood, pinNum, eachOrient)
        if didPlace!=None:
          ##print("testing&recursing w/o %s @ (%d,%d) in orient %d {" % (eachNood.getName(), \
               ##self.__pinList[pinNum][0], self.__pinList[pinNum][1], eachOrient))
          result += self.__checkAllHelper(noodleList[1:])
          ##print("\n}")
          self.unplacePiece(eachNood, pinNum, eachOrient)
    return result

  def checkAll(self):
    self.__iterProgress = 0
    self.getNumIters()
    return self.__checkAllHelper(self.__noodleList)
 
                          ################
                          # OPTIMIZATION #
                          ################

  def setPossPlaces(self):
    for eachNood in self.__noodleList:
      eachNood.numPossPlaces = 0
      eachNood.possPlacements = []
      for pinNum in range(len(self.__pinList)):
        for eachOrient in range(4 if eachNood.getSym() else 8):
          if self.tryToPlacePiece(eachNood, pinNum, eachOrient) != None:
            eachNood.numPossPlaces += 1
            eachNood.possPlacements.append((pinNum, eachOrient))
            self.unplacePiece(eachNood, pinNum, eachOrient)

  def sortByNumPlaces(self):
    self.setPossPlaces()
    self.__noodleList = sorted(self.__noodleList, \
                               key=lambda noodle: noodle.numPossPlaces) 

  def printPossPlaces(self):
    self.sortByNumPlaces()
    for eachNood in self.__noodleList:
      for eachPlace in eachNood.possPlacements:
        print("%s: pin %d, orient %d" % (eachNood.getName(), \
              eachPlace[0], eachPlace[1]))

  def getNumIters(self):
    self.sortByNumPlaces()
    self.__numIters = 1
    for eachNood in self.__noodleList:
      self.__numIters *= eachNood.numPossPlaces
    return self.__numIters

  def isPinOccupied(self, pinNum):
    result = False
    pinTup = self.__pinList[pinNum]
    for eachNood in self.__noodleList:
      if eachNood.getPinLoc()!=None and \
         eachNood.getPinLoc()[0]==pinTup[0] and eachNood.getPinLoc()[1]==pinTup[1]:
        result = True
    return result
     
#####################################################################
###########################  TO_STRING  #############################
#####################################################################
                          
  def __str__(self):
    retStr = ""
    for y in range(self.__size):
      for x in range(self.__size):
        if self.__isHole((x,y)):
          retStr += " \t"
        elif self.__isPinJustCoordCheck((x,y)):
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
