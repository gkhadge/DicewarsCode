# This file should define a class for a single hex tile on the map.
# They'll have a few methods used to obtain the position of a given tile
# and similar simple tasks.


###  TODO:  Add self.color

class Hexagon:
    # See above.

    ## xPos and yPos describe the position of the hex in coordinates.
    def __init__(self, xPos, yPos):
        self.xPos = xPos
        self.yPos = yPos

    def __repr__(self):
        return "Hexagon at: (" + str(self.xPos) + ", " + str(self.yPos) + ")"
