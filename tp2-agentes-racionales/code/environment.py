import random

#X hace referencia a las filas
#Y hace referencia a las columnas
class Environment:
    def __init__(self, sizeX, sizeY, dirtRate):
        self.sizeX = sizeX
        self.sizeY = sizeY
        #Porcentaje de casillas sucias
        self.dirtRate = dirtRate
        self.grid = [[0 for i in range(sizeY)] for j in range(sizeX)]
        #Lista con todas las posiciones del entorno
        self.positions = []
        for i in range(0, self.sizeX):
            for j in range(0, self.sizeY):
                self.positions.append((i, j))
        self.initDirt()
    
    #Crea los lugares sucios aleatoriamente en el grid
    def initDirt(self):
        totalSize = self.sizeX * self.sizeY
        totalDirt = int(self.dirtRate * totalSize)
        dirtyPositions = random.sample(self.positions, totalDirt)
        for i in dirtyPositions:
            self.grid[i[0]][i[1]] = 1
        return
    
    #Imprime por consola el entorno
    def printEnvironment(self):
        for i in range(self.sizeX):
            for j in range(self.sizeY):
                print(self.grid[i][j], end=" ")
            print(" ")
        return

    #Devuelve True si la posición está sucia (1), False si está limpia (0)
    def isDirty(self, x, y):
        if self.grid[x][y] == 1:
            return True
        else:
            return False

    #Devuelve True si es posible realizar la acción, False en caso contrario
    def acceptAction(self, action, x, y):
        if action == "Arriba":
            if x + 1 > (self.sizeX - 1):
                return False
            else:
                return True
        elif action == "Abajo":
            if x - 1 < 0:
                return False
            else:
                return True
        elif action == "Derecha":
            if y + 1 > (self.sizeY - 1):
                return False
            else:
                return True
        elif action == "Izquierda":
            if y - 1 < 0:
                return False
            else:
                return True
        elif action == "Limpiar":
            if self.isDirty(self, x, y) == True:
                self.grid[x][y] = 0
            return True
        else:
            return False
            