from queue import PriorityQueue
import random

class Agent:
    #Constructor
    def __init__(self):
        self.lives = 1000

    #Método que recorre el entorno en anchura
    def recorrerAnchura(self, scenary):
        desc = scenary.desc
        n = len(desc)
        #Se inicializa la frontera con la posición inicial
        frontier = []
        #Set auxiliar para mejorar la eficiencia temporal
        frontierAux = set()
        #Diccionario para guardar los padres de los nodos
        parentDict = {}
        #Se busca la posición inicial
        for i in range(0, n):
            for j in range(0, n):
                if desc[i][j] == "S":
                    frontier.append((i, j))
                    parentDict[(i, j)] = None
                    frontierAux.add((i, j))
        #Set para guardar los nodos explorados
        explored = set()
        #Variable para guardar la solución
        solution = None
        #Variable para detener el ciclo
        stop = False
        #Ciclo principal
        while not stop:
            # Si la frontera está vacía, se detiene el ciclo
            if frontier == []:
                stop = True
                break
            #Se obtiene el primer nodo de la frontera
            actNode = frontier.pop(0)
            #Se elimina el nodo de la frontera auxiliar
            frontierAux.discard(actNode)
            #Se añade el nodo a los nodos explorados
            explored.add(actNode)
            #Se determinan las acciones posibles desde el nodo actual
            actions = self.determinePossibleActions(actNode[0], actNode[1], n)
            for i in actions:
                newX, newY = self.action(actNode, i)
                childNode = (newX, newY)
                #Si el nodo es un agujero, se ignora
                if desc[newX][newY] == "H":
                    continue
                #Si el nodo no ha sido explorado y no está en la frontera, se añade a la frontera
                if (childNode not in explored) and (childNode not in frontierAux):
                    parentDict[childNode] = actNode
                    #Si el nodo es la meta, se detiene el ciclo
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

    #Método que recorre el entorno en profundidad
    def recorrerProfundidad(self, scenary):
        desc = scenary.desc
        n = len(desc)
        #Se inicializa la frontera con la posición inicial
        frontier = []
        #Set auxiliar para mejorar la eficiencia temporal
        frontierAux = set()
        #Diccionario para guardar los padres de los nodos
        parentDict = {}
        #Se busca la posición inicial
        for i in range(0, n):
            for j in range(0, n):
                if desc[i][j] == "S":
                    frontier.append((i, j))
                    parentDict[(i, j)] = None
                    frontierAux.add((i, j))
        #Set para guardar los nodos explorados
        explored = set()
        solution = None
        stop = False
        while not stop:
            # Si la frontera está vacía, se detiene el ciclo
            if frontier == []:
                stop = True
                break
            #Se obtiene el último nodo de la frontera
            actNode = frontier.pop()
            #Se elimina el nodo de la frontera auxiliar
            frontierAux.discard(actNode)
            #Se añade el nodo a los nodos explorados
            explored.add(actNode)
            #Se determinan las acciones posibles desde el nodo actual
            actions = self.determinePossibleActions(actNode[0], actNode[1], n)
            for i in actions:
                #Se obtiene la nueva posición
                newX, newY = self.action(actNode, i)
                childNode = (newX, newY)
                #Si el nodo es un agujero, se ignora
                if desc[newX][newY] == "H":
                    continue
                #Si el nodo no ha sido explorado y no está en la frontera, se añade a la frontera
                if (childNode not in explored) and (childNode not in frontierAux):
                    parentDict[childNode] = actNode
                    #Si el nodo es la meta, se detiene el ciclo
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

    #Método que recorre el entorno en profundidad limitada
    def recorrerProfundidadLimitada(self, scenary, maxDepth):
        desc = scenary.desc
        n = len(desc)
        #Se inicializa la frontera con la posición inicial
        frontier = []
        #Set auxiliar para mejorar la eficiencia temporal
        frontierAux = set()
        #Diccionario para guardar los padres de los nodos
        parentDict = {}
        #Se busca la posición inicial
        for i in range(0, n):
            for j in range(0, n):
                if desc[i][j] == "S":
                    frontier.append((i, j))
                    parentDict[(i, j)] = None
                    frontierAux.add((i, j))
        #Set para guardar los nodos explorados
        explored = set()
        solution = None
        stop = False
        #Variable para guardar la profundidad
        depth = 0
        while not stop:
            # Si la frontera está vacía, se detiene el ciclo
            if frontier == []:
                stop = True
                break
            #Se obtiene el último nodo de la frontera
            actNode = frontier.pop()
            #Se elimina el nodo de la frontera auxiliar
            frontierAux.discard(actNode)
            #Se añade el nodo a los nodos explorados
            explored.add(actNode)
            #Se determinan las acciones posibles desde el nodo actual
            actions = self.determinePossibleActions(actNode[0], actNode[1], n)
            #Si no hay acciones posibles, se disminuye la profundidad
            if actions == []:
                depth = depth - 1
                continue
            else:
                #Se aumenta la profundidad
                depth = depth + 1

            #Si la profundidad es mayor a la máxima, se disminuye y se continúa
            if depth > maxDepth:
                depth = depth - 1
                continue
            for i in actions:
                newX, newY = self.action(actNode, i)
                childNode = (newX, newY)
                #Si el nodo es un agujero, se ignora
                if desc[newX][newY] == "H":
                    continue
                #Si el nodo no ha sido explorado y no está en la frontera, se añade a la frontera
                if (childNode not in explored) and (childNode not in frontierAux):
                    #Se añade el nodo al diccionario de padres
                    parentDict[childNode] = actNode
                    #Si el nodo es la meta, se detiene el ciclo
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

    #Método que recorre el entorno con el algoritmo de costo uniforme    
    def recorrerCostoUniforme(self, scenary, costOption):
        desc = scenary.desc
        n = len(desc)
        #Se inicializa la frontera con la posición inicial y una cola de prioridad
        frontier = PriorityQueue()
        #Diccionario para guardar los padres de los nodos
        parentDict = {}
        #Diccionario para guardar las prioridades de los nodos
        priorityDict = {}
        #Set auxiliar para mejorar la eficiencia temporal
        frontierAux = set()
        #Se busca la posición inicial
        for i in range(0, n):
            for j in range(0, n):
                if desc[i][j] == "S":
                    frontier.put((0, (i, j)))
                    parentDict[(i, j)] = None
                    frontierAux.add((i, j))
                    priorityDict[(i, j)] = 0
        #Set para guardar los nodos explorados
        explored = set()
        solution = None
        stop = False

        while not stop:
            # Si la frontera está vacía, se detiene el ciclo
            if frontier.empty():
                stop = True
                break
            #Se obtiene el primer nodo de la frontera con menor prioridad
            priority, actNode = frontier.get()
            frontierAux.discard(actNode)
            #Se añade el nodo a los nodos explorados
            explored.add(actNode)
            #Si el nodo es la meta, se detiene el ciclo
            if desc[actNode[0]][actNode[1]] == "G":
                solution = actNode
                stop = True
                break
            #Se determinan las acciones posibles desde el nodo actual
            actions = self.determinePossibleActions(actNode[0], actNode[1], n)

            for i in actions:
                newX, newY = self.action(actNode, i)
                childNode = (newX, newY)
                #Si el nodo es un agujero, se ignora
                if desc[newX][newY] == "H":
                    continue
                #Se calcula la prioridad del nodo hijo
                if costOption == 1:
                    childPriority = priority + 1
                else:
                    childPriority = priority + i + 1
                #Si el nodo no ha sido explorado y no está en la frontera, se añade a la frontera
                if (childNode not in explored) and (childNode not in frontierAux):
                    #Se añade el nodo al diccionario de padres
                    parentDict[childNode] = actNode
                    #Se añade el nodo a la frontera
                    frontier.put((childPriority, childNode))
                    #Se añade la prioridad al diccionario de prioridades
                    priorityDict[childNode] = childPriority
                    frontierAux.add(childNode)
                else:
                    #Si la prioridad del nodo actual es mayor a la calculada en el nuevo, se reemplaza
                    if priorityDict[childNode] > childPriority:
                        #Se reemplaza el nodo en la frontera y el padre en el diccionario
                        frontier, parentDict = self.replacePriorityItem(frontier, childNode, childPriority, parentDict, actNode)
                        #Se reemplaza la prioridad en el diccionario
                        priorityDict[childNode] = childPriority
        if solution == None:
            return [], [], []
        else:
            return self.createPath(parentDict, solution, explored)

    #Método que recorre el entorno con el algoritmo A*
    def aEstrella(self, scenary, costOption):
        desc = scenary.desc
        n = len(desc)
        #Se inicializa la frontera con la posición inicial y una cola de prioridad
        frontier = PriorityQueue()
        #Diccionario para guardar las prioridades de los nodos
        priorityDict = {}
        #Diccionario para guardar los padres de los nodos
        parentDict = {}
        goal = None
        #Set auxiliar para mejorar la eficiencia temporal
        frontierAux = set()
        #Se busca la posición inicial y la meta
        for i in range(0, n):
            for j in range(0, n):
                if desc[i][j] == "S":
                    frontier.put((0, (i, j)))
                    parentDict[(i, j)] = None
                    frontierAux.add((i, j))
                    priorityDict[(i, j)] = 0
                if desc[i][j] == "G":
                    goal = (i, j)
        #Set para guardar los nodos explorados
        explored = set()
        solution = None
        stop = False
        while not stop:
            # Si la frontera está vacía, se detiene el ciclo
            if frontier.empty():
                stop = True
                break
            #Se obtiene el primer nodo de la frontera con menor prioridad
            priority, actNode = frontier.get()
            frontierAux.discard(actNode)
            #Se añade el nodo a los nodos explorados
            explored.add(actNode)
            #Si el nodo es la meta, se detiene el ciclo
            if desc[actNode[0]][actNode[1]] == "G":
                solution = actNode
                stop = True
                break
            #Se determinan las acciones posibles desde el nodo actual
            actions = self.determinePossibleActions(actNode[0], actNode[1], n)
            for i in actions:
                newX, newY = self.action(actNode, i)
                childNode = (newX, newY)
                #Si el nodo es un agujero, se ignora
                if desc[newX][newY] == "H":
                    continue
                #Se calcula la prioridad del nodo hijo, esto se hace con la función heurística, la cual se implementa utilizando la distancia Manhattan
                if costOption == 1:
                    #Se calcula la prioridad con la función heurística
                    childPriority = priority + self.heuristic(childNode, goal)
                else:
                    #Se calcula la prioridad con la función heurística para el segundo caso, utilizando el costo de la acción
                    childPriority = priority + i + self.heuristic(childNode, goal)

                #Si el nodo no ha sido explorado y no está en la frontera, se añade a la frontera
                if (childNode not in explored) and (childNode not in frontierAux):
                    parentDict[childNode] = actNode
                    frontier.put((childPriority, childNode))
                    frontierAux.add(childNode)
                    priorityDict[childNode] = childPriority
                else:
                    #Si la prioridad del nodo actual es mayor a la calculada en el nuevo, se reemplaza
                    if priorityDict[childNode] > childPriority:
                        #Se reemplaza el nodo en la frontera y el padre en el diccionario
                        frontier, parentDict = self.replacePriorityItem(frontier, childNode, childPriority, parentDict, actNode)
                        priorityDict[childNode] = childPriority
        if solution == None:
            return [], [], []
        else:
            return self.createPath(parentDict, solution, explored)
    
    #Método que recorre el entorno de forma aleatoria
    def recorrerAleatorio(self, scenary):
        desc = scenary.desc
        n = len(desc)
        explored = []
        #Se busca la posición inicial
        for i in range(0, n):
            for j in range(0, n):
                if desc[i][j] == "S":
                    explored.append((i, j))
                    actualNode = (i, j)
        #Variable para contar las acciones realizadas
        action = 0
        stop = False
        solution = False
        directions = []
        while not stop:
            action += 1
            #Si se superan las 1000 acciones, se detiene el ciclo
            if action > 1000:
                stop = True
                solution = False
                break
            #Si se llega a la meta, se detiene el ciclo
            if desc[actualNode[0]][actualNode[1]] == "G":
                stop = True
                solution = True
                break
            #Se determinan las acciones posibles desde el nodo actual
            actions = self.determinePossibleActions(actualNode[0], actualNode[1], n)
            #Si no hay acciones posibles, se detiene el ciclo
            if actions == []:
                stop = True
                solution = False
            #Se elige una acción aleatoria
            option = random.randint(0, len(actions) - 1)
            #Se obtiene la nueva posición
            newX, newY = self.action(actualNode, actions[option])
            actualNode = (newX, newY)
            directions.append(actions[option])

        if solution == False:
            return [], [], []
        else:
            return explored, directions, explored

    #Método que calcula la heurística utilizando la distancia Manhattan
    def heuristic(self, node, goal):
        return abs(node[0] - goal[0]) + abs(node[1] - goal[1])
    
    #Método que reemplaza un nodo en la cola de prioridad
    def replacePriorityItem(self, queue, elem, priority, parentDict, actNode):
        auxList = []
        while queue.empty() == False:
            prioridad, item = queue.get()
            #Si se encuentra el nodo, se reemplaza
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
    
    #Método que verifica si un elemento está en la cola de prioridad. No se utiliza en el código principal
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

    #Método que crea el camino a seguir. Va desde la meta hasta el inicio utilizando el diccionario de padres
    def createPath(self, parentDict, solution, explored):
        path = []
        directions = []
        actNode = solution
        while actNode != None:
            parentNode = parentDict[actNode]
            #Si el nodo no tiene padre, se añade a la lista de nodos y se detiene el ciclo
            if parentNode == None:
                path.insert(0, (actNode[0], actNode[1]))
                actNode = None
            else:
                #Si el nodo tiene padre, se añade a la lista de nodos y se actualiza el nodo actual
                path.insert(0, (actNode[0], actNode[1]))
                directions.insert(0, self.getDirections(parentNode[0], parentNode[1], actNode[0], actNode[1]))
                actNode = parentNode
        return path, directions, explored
        
    #Método que determina la dirección a seguir en base a la posición de los dos nodos. 0: Izquierda, 1: Abajo, 2: Derecha, 3: Arriba
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
    
    #Método que realiza una acción en base a un nodo y una acción
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
    
    #Método que determina las acciones posibles desde un nodo teniendo en cuenta el tamaño del entorno
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
    
    #Método que cuenta las acciones realizadas. Simplemente suma las acciones + 1
    def countActions(self, directions):
        sum = 0
        for i in directions:
            sum = sum + i + 1
        return sum


        
