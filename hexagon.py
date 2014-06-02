# This file should define a class for a single hex tile on the map.
# They'll have a few methods used to obtain adjacent hexes and to obtain
# the position of a given tile.


###  TODO:  Add self.color and adjacency and path methods.  Or perhaps those
###  should be in a map class?

class Hexagon:
    # See above.

    ## xPos and yPos describe the position of the hex in axial coordinates.
    def __init__(self, xPos, yPos, apothem):
        self.xPos = xPos
        self.yPos = yPos
        self.size = apothem

    def __repr__(self):
        return "Hexagon at: (" + str(self.xPos) + ", " + str(self.yPos) + ") with size: " + str(self.size)
