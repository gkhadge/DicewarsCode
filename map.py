# This file should define a pretty large and all-encompassing class - the map.
# It will include most of the machinery for the map itself.
# Effectively, the structure of a map is simply a 2-D array of hexagons.

# There should be methods for finding adjacent hexagons to a hexagon,
# returning the hex distance between hexagons, and finding a path of hexagons
# between any two given hexagons.

# Build this to be expanded, we're probably going to add a lot more to it.

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
        
        row = []*(yMax - yMin)
        self.grid = [row]*(xMax - xMin)
        for hex in hexList:
            self.grid[hex.xPos, hex.yPos] = hex

    def adjacency(self, hex):
        # Returns a list of all adjacent hexagons to hex.
        xPos = hex.xPos + self.xMin
        yPos = hex.yPos + self.yMin

        hex1 = self.grid[xPos - 1][yPos]
        hex2 = self.grid[xPos + 1][yPos]
        hex3 = self.grid[xPos][yPos - 1]
        hex4 = self.grid[xPos][yPos + 1]
        hex5 = self.grid[xPos - 1][yPos + 1]
        hex6 = self.grid[xPos + 1][yPos - 1]

        return [hex1, hex2, hex3, hex4, hex5, hex6]
        

        
