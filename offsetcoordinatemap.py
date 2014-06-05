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

    def __init__(self):
        # hexList is a list containing hexagons.

        # There's got to be a better way to do this.
        self.ROWS = 28
        self.COLS = 32

        # Store hexagons in 2D array, "grid"       
        self.grid = [[0 for x in xrange(self.COLS)] for x in xrange(self.ROWS)]
        
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
