from Node import Node

""" The Astar algorithm"""

def algorithm(grid, start, end):
    # Create start and end node

    startNode = Node(None, start)
    startNode.gCost = startNode.hCost = startNode.fCost = 0
    endNode = Node(None, end)
    endNode.gCost = endNode.hCost = endNode.fCost = 0

    # Initialize both open and closed list
    openList = []
    closedList = []
    openList.append(startNode)

    # Loop until you find the end node
    while len(openList) > 0:
        currentNode = openList[0]
        currentIndex = 0

        for index, item in enumerate(openList):
            if item.fCost < currentNode.fCost:
                currentNode = item
                currentIndex = index

        # add to closed list
        openList.pop(currentIndex)
        closedList.append(currentNode)

        # reach the Destination
        if currentNode == endNode:
            path = []
            current = currentNode

            while current is not None:
                path.append(current.position)
                current = current.parent
            # Return reversed path
            return path[::-1] 

        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:

            node_position = (currentNode.position[0] + new_position[0], currentNode.position[1] + new_position[1])

            # Make sure is within range
            if node_position[0] > (len(grid) - 1) or node_position[0] < 0 or node_position[1] > (len(grid[len(grid)-1]) -1) or node_position[1] < 0:
                continue

            # Make sure walkable 
            if grid[node_position[0]][node_position[1]] != 0:
                continue

            # Create a new node
            new_node = Node(currentNode, node_position)
            children.append(new_node)
        for child in children:
            for closed_child in closedList:
                if child == closed_child:
                    continue

            # Create the f, g, and h values
            child.gCost = currentNode.gCost + 1
            child.hCost = ((child.position[0] - endNode.position[0]) ** 2) + ((child.position[1] - endNode.position[1]) ** 2)
            child.fCost = child.gCost + child.hCost
            for openNode in openList:
                if child == openNode and child.gCost > openNode.gCost:
                    continue
            openList.append(child)

