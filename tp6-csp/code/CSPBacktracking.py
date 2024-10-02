class CSPBacktracking:
    def __init__(self, n):
        #Iteraciones hasta encontrar solución
        self.iteration = 0;
        #Almacenamiento de la solución
        self.actualSolution = [None] * n;
        #Tamaño del tablero
        self.n = n;

    #Función para llamar a la parte recursiva
    def solveCsp(self):
        #Si condition es True, se encontró solución y se devuelve, caso contrario se devuelve False
        condition = self.cspBacktracking(0)
        if condition == True:
            return self.actualSolution
        else:
            return False

    #Parte recursiva de la implementación
    def cspBacktracking(self, actualRow):
        if actualRow == self.n:
            return True;
        for i in range(0, self.n):
            self.iteration += 1;
            #Se verifica si para la columna i la solución satisface las restricciones
            if self.h(actualRow, i):
                #Si satisface, se agrega la solución al tablero
                self.actualSolution[actualRow] = i
                #Se continúa con la siguiente columna recursivamente
                condition = self.cspBacktracking(actualRow + 1)
                #Si la condición es igual a True (se encontró solución) se retorna True, caso contrario se sigue con el bucle
                if condition == True:
                    return True
        return False

    #Función para verificar restricciones. i es la fila y j es la columna.
    #Modificada del tp 5 
    def h(self, i, j):
        #Solo hay que verificar hasta la fila actual porque el resto no se ha recorrido todavía
        for k in range(0, i):
            if self.actualSolution[k] == j or abs(j - self.actualSolution[k]) == abs(i - k):
                #Hay conflictos y se retorna false
                return False
        return True