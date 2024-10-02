class CSPForwardChecking:
    def __init__(self, n):
        #Iteraciones hasta encontrar solución
        self.iteration = 0;
        #Almacenamiento de la solución
        self.actualSolution = [None] * n;
        #Lista con los posibles valores para cada fila
        self.possibleValues = [set(range(n)) for _ in range(n)]
        #Cantidad posible de valores que puede tomar
        self.possibleValuesNumber = [n] * n;
        #Tamaño del tablero
        self.n = n;

    #Devuelve la fila con menos valores posibles
    def minRow(self):
        minIndex = None
        for i in range(0, self.n):
            if self.possibleValuesNumber[i] == None:
                continue
            if minIndex == None:
                min = self.possibleValuesNumber[i]
                minIndex = i
            else:
                if self.possibleValuesNumber[i] < min:
                    min = self.possibleValuesNumber[i]
                    minIndex = i
        self.possibleValuesNumber[minIndex] = None
        return minIndex
    
    #Función para llamar a la parte recursiva
    def solveCsp(self):
        #Si condition es True, se encontró solución y se devuelve, caso contrario se devuelve False
        condition = self.cspForwardChecking(0)
        if condition == True:
            return self.actualSolution
        else:
            return False

    #Parte recursiva de la implementación
    def cspForwardChecking(self, actualRow):
        if actualRow == self.n:
            return True;
        
        for i in self.possibleValues[actualRow]:
            self.iteration += 1;
            #Se verifica si para la columna i la solución satisface las restricciones
            if self.h(actualRow, i):
                #Lista auxiliar con los posibles valores actuales
                auxPossibleValues = [set(subset) for subset in self.possibleValues]
                auxPossibleValuesNumber = self.possibleValuesNumber.copy();
                #Eliminar valores de las demas filas teniendo en cuenta restricciones
                self.calculateForwardChecking(actualRow, i)
                #Si satisface, se agrega la solución al tablero
                self.actualSolution[actualRow] = i
                #Se continúa con la siguiente columna recursivamente
                condition = self.cspForwardChecking(actualRow + 1)
                #Si la condición es igual a True (se encontró solución) se retorna True, caso contrario se sigue con el bucle
                if condition == True:
                    return True
                #Se restauran los posibles valores
                self.possibleValues = auxPossibleValues;
                self.possibleValuesNumber = auxPossibleValuesNumber

        return False

    #Calcular y modificar los valores posibles de las otras filas teniendo en cuenta las restricciones
    def calculateForwardChecking(self, actualRow, j):
        aux = 1
        for k in range(actualRow + 1, self.n):
            if j in self.possibleValues[k]:
                self.possibleValues[k].discard(j)
                self.possibleValuesNumber[k] -= 1
            backDiagonal = j - aux;
            forwardDiagonal = j + aux;
            if backDiagonal > 0:
                if backDiagonal in self.possibleValues[k]:
                    self.possibleValues[k].discard(backDiagonal)
                    self.possibleValuesNumber[k] -= 1
            if forwardDiagonal < self.n:
                if forwardDiagonal in self.possibleValues[k]:
                    self.possibleValues[k].discard(forwardDiagonal)
                    self.possibleValuesNumber[k] -= 1
            aux += 1;
        return

    #Función para verificar restricciones. i es la fila y j es la columna.
    #Modificada del tp 5 
    def h(self, i, j):
        #Solo hay que verificar hasta la fila actual porque el resto no se ha recorrido todavía
        for k in range(0, i):
            if self.actualSolution[k] == j or abs(j - self.actualSolution[k]) == abs(i - k):
                #Hay conflictos y se retorna false
                return False
        return True