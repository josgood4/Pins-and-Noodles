class Board():

  def __init__(self, pinList, size, noodleList):
    self.pinList = pinList
    self.size = size
    self.noodleList = noodleList

  def isPin(self, coord):
    for eachPin in self.pinList:
      if coord[0] == eachPin[0] and coord[1] == eachPin[1]:
        return True
    return False

  def isInBounds(self, coord):
    return coord[0]>=0 and coord[1]>=0 and coord[0]<self.size and coord[1]<self.size


