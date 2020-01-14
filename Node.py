class Node():
    #A node class for the A star Pathfinding

    def __init__(self, parent=None, position=None):

        self.parent = parent
        self.position = position

        #is the distance between the node
        self.gCost = 0
        #h cost is also called heuristc value (estimated value)
        self.hCost = 0
        #f cost is gCost + hCost
        self.fCost = 0

    def __eq__(self, other):
        return self.position == other.position