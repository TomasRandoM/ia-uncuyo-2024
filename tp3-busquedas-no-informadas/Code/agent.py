from queue import PriorityQueue

class Agent:
    def __init__(self):
        self.lives = 1000

    def recorrerAnchura(self, scenary):
        desc = scenary.desc
        n = len(desc)
        frontier = []
        frontierAux = set()
        parentDict = {}
        for i in range(0, n):
            for j in range(0, n):
                if desc[i][j] == "S":
                    frontier.append((i, j))
                    parentDict[(i, j)] = None
                    frontierAux.add((i, j))
        explored = set()
        solution = None
        stop = False
        while not stop:
            if frontier == []:
                stop = True
                break
            actNode = frontier.pop(0)
            frontierAux.discard(actNode)
            explored.add(actNode)

            actions = self.determinePossibleActions(actNode[0], actNode[1], n)
            for i in actions:
                newX, newY = self.action(actNode, i)
                childNode = (newX, newY)
                if desc[newX][newY] == "H":
                    continue
                if (childNode not in explored) and (childNode not in frontierAux):
                    parentDict[childNode] = actNode
                    if desc[newX][newY] == "G":
                        solution = childNode
                        stop = True
                        break
                    else:
                        frontier.append(childNode)
                        frontierAux.add(childNode)
        if solution == None:
            return [], [], []
        else:
            return self.createPath(parentDict, solution, explored)


    def recorrerProfundidad(self, scenary):
        desc = scenary.desc
        n = len(desc)
        frontier = []
        frontierAux = set()
        parentDict = {}
        for i in range(0, n):
            for j in range(0, n):
                if desc[i][j] == "S":
                    frontier.append((i, j))
                    parentDict[(i, j)] = None
                    frontierAux.add((i, j))
        explored = set()
        solution = None
        stop = False
        while not stop:
            if frontier == []:
                stop = True
                break
            actNode = frontier.pop()
            frontierAux.discard(actNode)
            explored.add(actNode)

            actions = self.determinePossibleActions(actNode[0], actNode[1], n)
            for i in actions:
                newX, newY = self.action(actNode, i)
                childNode = (newX, newY)
                if desc[newX][newY] == "H":
                    continue
                if (childNode not in explored) and (childNode not in frontierAux):
                    parentDict[childNode] = actNode
                    if desc[newX][newY] == "G":
                        solution = childNode
                        stop = True
                        break
                    else:
                        frontier.append(childNode)
                        frontierAux.add(childNode)
        if solution == None:
            return [], [], []
        else:
            return self.createPath(parentDict, solution, explored)

    def recorrerProfundidadLimitada(self, scenary, maxDepth):
        desc = scenary.desc
        n = len(desc)
        frontier = []
        frontierAux = set()
        parentDict = {}
        for i in range(0, n):
            for j in range(0, n):
                if desc[i][j] == "S":
                    frontier.append((i, j))
                    parentDict[(i, j)] = None
                    frontierAux.add((i, j))
        explored = set()
        solution = None
        stop = False
        depth = 0
        while not stop:
            if frontier == []:
                stop = True
                break
            actNode = frontier.pop()
            frontierAux.discard(actNode)
            explored.add(actNode)

            actions = self.determinePossibleActions(actNode[0], actNode[1], n)
            if actions == []:
                depth = depth - 1
                continue
            else:
                depth = depth + 1

            if depth > maxDepth:
                depth = depth - 1
                continue
            for i in actions:
                newX, newY = self.action(actNode, i)
                childNode = (newX, newY)
                if desc[newX][newY] == "H":
                    continue
                if (childNode not in explored) and (childNode not in frontierAux):
                    parentDict[childNode] = actNode
                    if desc[newX][newY] == "G":
                        solution = childNode
                        stop = True
                        break
                    else:
                        frontier.append(childNode)
                        frontierAux.add(childNode)
        if solution == None:
            return [], [], []
        else:
            return self.createPath(parentDict, solution, explored)
        
    def recorrerCostoUniforme(self, scenary, costOption):
        desc = scenary.desc
        n = len(desc)
        frontier = PriorityQueue()
        parentDict = {}
        priorityDict = {}
        frontierAux = set()
        for i in range(0, n):
            for j in range(0, n):
                if desc[i][j] == "S":
                    frontier.put((0, (i, j)))
                    parentDict[(i, j)] = None
                    frontierAux.add((i, j))
                    priorityDict[(i, j)] = 0
        explored = set()
        solution = None
        stop = False

        while not stop:
            if frontier.empty():
                stop = True
                break

            priority, actNode = frontier.get()
            frontierAux.discard(actNode)

            explored.add(actNode)
            if desc[actNode[0]][actNode[1]] == "G":
                solution = actNode
                stop = True
                break

            actions = self.determinePossibleActions(actNode[0], actNode[1], n)

            for i in actions:
                newX, newY = self.action(actNode, i)
                childNode = (newX, newY)
                if desc[newX][newY] == "H":
                    continue
                
                if costOption == 1:
                    childPriority = priority + 1
                else:
                    childPriority = priority + i + 1
             
                if (childNode not in explored) and (childNode not in frontierAux):
                    parentDict[childNode] = actNode
                    frontier.put((childPriority, childNode))
                    priorityDict[childNode] = childPriority
                    frontierAux.add(childNode)
                else:
                    if priorityDict[childNode] > childPriority:
                        frontier, parentDict = self.replacePriorityItem(frontier, childNode, childPriority, parentDict, actNode)
                        priorityDict[childNode] = childPriority
        if solution == None:
            return [], [], []
        else:
            return self.createPath(parentDict, solution, explored)

    def aEstrella(self, scenary, costOption):
        desc = scenary.desc
        n = len(desc)
        frontier = PriorityQueue()
        priorityDict = {}
        parentDict = {}
        goal = None
        frontierAux = set()
        for i in range(0, n):
            for j in range(0, n):
                if desc[i][j] == "S":
                    frontier.put((0, (i, j)))
                    parentDict[(i, j)] = None
                    frontierAux.add((i, j))
                    priorityDict[(i, j)] = 0
                if desc[i][j] == "G":
                    goal = (i, j)
        explored = set()
        solution = None
        stop = False
        while not stop:
            if frontier.empty():
                stop = True
                break

            priority, actNode = frontier.get()
            frontierAux.discard(actNode)

            explored.add(actNode)

            if desc[actNode[0]][actNode[1]] == "G":
                solution = actNode
                stop = True
                break

            actions = self.determinePossibleActions(actNode[0], actNode[1], n)
            for i in actions:
                newX, newY = self.action(actNode, i)
                childNode = (newX, newY)
                if desc[newX][newY] == "H":
                    continue
                
                if costOption == 1:
                    childPriority = priority + self.heuristic(childNode, goal)
                else:
                    childPriority = priority + i + 1 + self.heuristic(childNode, goal)
             
                if (childNode not in explored) and (childNode not in frontierAux):
                    parentDict[childNode] = actNode
                    frontier.put((childPriority, childNode))
                    frontierAux.add(childNode)
                    priorityDict[childNode] = childPriority
                else:
                    if priorityDict[childNode] > childPriority:
                        frontier, parentDict = self.replacePriorityItem(frontier, childNode, childPriority, parentDict, actNode)
                        priorityDict[childNode] = childPriority
        if solution == None:
            return [], [], []
        else:
            return self.createPath(parentDict, solution, explored)

    def heuristic(self, node, goal):
        return abs(node[0] - goal[0]) + abs(node[1] - goal[1])
    
    def replacePriorityItem(self, queue, elem, priority, parentDict, actNode):
        auxList = []
        while queue.empty() == False:
            prioridad, item = queue.get()
            
            if item == elem:
                if prioridad > priority:
                    auxList.append((priority, elem))
                    parentDict[elem] = actNode
                break
            else:
                auxList.append((prioridad, item))
        for i in auxList:
            queue.put(i)
        return queue, parentDict
    
    def isInPriorityQueue(self, queue, elem):
        state = False
        auxList = []
        while queue.empty() == False:
            prioridad, item = queue.get()
            auxList.append((prioridad, item))
            if item == elem:
                state = True
        
        for i in auxList:
            queue.put(i)
        return state


    def createPath(self, parentDict, solution, explored):
        path = []
        directions = []
        actNode = solution
        while actNode != None:
            parentNode = parentDict[actNode]
            if parentNode == None:
                path.insert(0, (actNode[0], actNode[1]))
                actNode = None
            else:
                path.insert(0, (actNode[0], actNode[1]))
                directions.insert(0, self.getDirections(parentNode[0], parentNode[1], actNode[0], actNode[1]))
                actNode = parentNode
        return path, directions, explored
        
    
    def getDirections(self, oldX, oldY, newX, newY):
        if oldX == newX:
            if oldY < newY:
                return 2
            else:
                return 0
        else:
            if oldX < newX:
                return 1
            else:
                return 3
            
    def action(self, node, action):
        x = node[0]
        y = node[1]
        if action == 0:
            y = y - 1
        elif action == 1:
            x = x + 1
        elif action == 2:
            y = y + 1
        elif action == 3:
            x = x - 1
        else:
            raise ValueError("La acción ingresada no es correcta")
        return x, y
    
    def determinePossibleActions(self, posX, posY, size):
        actions = []
        if posY != 0:
            actions.append(0)
        if posX != (size - 1):
            actions.append(1)
        if posY != (size - 1):
            actions.append(2)
        if posX != 0:
            actions.append(3)
        return actions
    
    def countActions(self, directions):
        sum = 0
        for i in directions:
            sum = sum + i + 1
        return sum


        
