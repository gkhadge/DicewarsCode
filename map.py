# This file should define a pretty large and all-encompassing class - the map.
# It will include most of the machinery for the map itself.
# Effectively, the structure of a map is simply a 2-D array of hexagons.

# There should be methods for finding adjacent hexagons to a hexagon,
# returning the hex distance between hexagons, and finding a path of hexagons
# between any two given hexagons.

# Build this to be expanded, we're probably going to add a lot more to it.


#         o
#      o     o
#   o           o                   o
#   o           o                     o
#   o           o    ---->              o 
#   o           o                         V   
#      o     o     +x direction    +y direction 
#         o 
# Class uses axial coordinates with pointy-topped hexagons
# See link for more details
# http://www.redblobgames.com/grids/hexagons/

# See for code organization and discussion:
# https://docs.google.com/a/g.hmc.edu/document/d/1qaDAmrd0Lflz5zCO4VxH2M4TKGrQX58B_4DWbv6YZWk/edit


class Map:
    # See above.

    def __init__(self, hexList):
        # hexList is a list containing hexagons.

        # There's got to be a better way to do this.
        xMax = 0
        xMin = 0
        yMax = 0
        yMin = 0
        for hex in hexList:
            if hex.xPos > xMax:
                xMax = hex.xPos
            elif hex.xPos < xMin:
                xMin = hex.xPos
            if hex.yPos > yMax:
                yMax = hex.yPos
            elif hex.yPos < yMin:
                yMin = hex.yPos

        self.xMin = xMin
        self.yMin = yMin

        # Store hexagons in 2D array, "grid"
        # row index represents x distance from xmin (xPos-xMin)
        # col index represents y distance from ymin (yPos-yMin)        
        row = []*(yMax - yMin)
        self.grid = [row]*(xMax - xMin)
        for hex in hexList:
            self.grid[hex.xPos-self.xMin, hex.yPos-self.yMin] = hex

    def adjacency(self, hex):
        # Returns a list of all adjacent hexagons to hex.

        # Indices of hex in self.grid
        xIndex = hex.xPos - self.xMin
        yIndex = hex.yPos - self.yMin

        # Going CCW
        hex1 = self.grid[xIndex + 1][yIndex]     # right
        hex2 = self.grid[xIndex + 1][yIndex - 1] # upper right
        hex3 = self.grid[xIndex][yIndex - 1]     # upper left
        hex4 = self.grid[xIndex - 1][yIndex]     # left
        hex5 = self.grid[xIndex - 1][yIndex + 1] # lower left
        hex6 = self.grid[xIndex][yIndex + 1]     # lower right 

        return [hex1, hex2, hex3, hex4, hex5, hex6]        
