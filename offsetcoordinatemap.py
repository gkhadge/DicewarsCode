# modified version to be offset coordinates

# This file should define a pretty large and all-encompassing class - the map.
# It will include most of the machinery for the map itself.
# Effectively, the structure of a map is simply a 2-D array of hexagons.

# There should be methods for finding adjacent hexagons to a hexagon,
# returning the hex distance between hexagons, and finding a path of hexagons
# between any two given hexagons.

# Build this to be expanded, we're probably going to add a lot more to it.


#         o                 o
#      o     o                o
#   o           o           o
#   o           o             o  
#   o           o           o          ----> 
#   o           o             v   
#      o     o          +x direction +y direction 
#         o 
# Class uses odd row offset coordinates with pointy-topped hexagons
# See link for more details
# http://www.redblobgames.com/grids/hexagons/

# See for code organization and discussion:
# https://docs.google.com/a/g.hmc.edu/document/d/1qaDAmrd0Lflz5zCO4VxH2M4TKGrQX58B_4DWbv6YZWk/edit

## Directions
SR = 0 # Straight Right
UR = 1 # Upper Right
UL = 2 # Upper Left
SL = 3 # Straight Left
LL = 4 # Lower Left
LR = 5 # Lower Right

## Error code
INVALID = -1

class Map2:
    # See above.

    def __init__(self, numRows, numCols, hexList):
        # hexList is a list containing hexagons.

        # There's got to be a better way to do this.
        self.ROWS = numRows
        self.COLS = numCols

        self.grid = [[0 for y in xrange(self.COLS)] for x in xrange(self.ROWS)]
        # Store hexagons in 2D array, "grid"
        for x in xrange(self.ROWS):
            for y in xrange(self.COLS):
                for hexagon in hexList:
                    if (hexagon.xPos == x) and (hexagon.yPos == y):
                        self.grid[x][y] = hexagon
                        # It might be worth it to remove hexagon from hexList,
                        # but I'd expect weird behavior if we do that.

    def setHexToPos(self, x, y, hexagon):
        # Sets the item in self.grid at (x,y) to hexagon
        # Assumes that x and y are in range

        self.grid[x][y] = hexagon
        return ''

        
    def neighbor(self, x, y, direction):
        # Returns state of hexagon in the direction of direction
        # direction = [0,1,2,3,4,5]
        # output = -1 if invalid
        #        = 0 if unoccupied
        #        = 1,2,3,4,5,6,7,8 if occupied by
        #        red, orange, yellow, lime, green, teal, purple, pink
        
        if direction < 0 or direction > 5:
            print "Invalid Direction"
            return INVALID


        neighbors = [[ [0,  1], [ -1, 0], [-1, -1],[0,  -1], [1, -1], [1, 0] ], \
                     [ [0,  1], [ -1, 1], [-1,  0],[0,  -1], [1,  0], [1, 1] ] ]
        # note I use & 1 but mod 2 would work if it never returns -1
        parity = y & 1
        d = neighbors[parity][direction]
        newx = x + d[0]
        newy = y + d[1]
        print str(newx) + ", " + str(newy) 
        if newx < 0 or newx >= self.ROWS or newy < 0 or newy >= self.COLS:
            return INVALID
        return self.grid[newx][newy]

    def neighborList(self, x, y):
        # Returns a list of all hexagons adjacent to the hexagon stored in x, y
        result = []
        for i in xrange(5):
            result.append(self.neighbor(x, y, i))
        return result

    def oddRowOffsetToCube(self, r, q):
        # Takes the input coordinates in (r,q) in odd row offset to cube coordinates.

        x = q - (r - (r&1)) / 2
        z = r
        y = -1 * x - z
        return [x, y, z]

    def cubeToAxial(self, x, y, z):
        # Takes the input coordinates in (x,y,z) cube to axial coordinates.

        q = x
        r = z
        return [r, q]

    def oddRowOffsetToAxial(self, r, q):
        # Takes the input coordinates in (r,q) odd row offset to axial coordinates.

        cubeCoord = self.oddRowOffsetToCube(r, q)
        result = self.cubeToAxial(cubeCoord[0], cubeCoord[1], cubeCoord[2])
        return result

    def axialToCube(self, r, q)
        # Takes the input coordinates in (r,q) axial to cube coordinates.

        x = q
        z = r
        y = -1 * x - z
        return [x, y, z]

    def cubeToOddRowOffset(self, x, y, z):
        # Takes the input coordinates in (x,y,z) cube to odd row offset.

        q = x + (z - (z&1)) / 2
        r = z
        return [r, q]

    def axialToOddRowOffset(self, z, x):
        # Takes the input coordinates (z, x) axial to odd row offset.

        cubeCoord = self.axialToCube(z,x)
        result = self.cubeToOddRowOffset(self, cubeCoord[0], cubeCoord[1], cubeCoord[2])
        return result























        
