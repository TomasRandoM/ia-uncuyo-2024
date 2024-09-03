import gymnasium as gym
import random
from gymnasium import wrappers

class Environment:
    def __init__(self, size, iceProb, isSlippery = False):
        #Se genera un entorno con un tamaño y probabilidad de hielo específicos
        self.env, self.desc = self.generate_random_map_custom(size, iceProb, slippery=isSlippery)
        #Se limita la cantidad de pasos que puede dar el agente a 1000
        self.env = wrappers.TimeLimit(self.env.env, 1000)

    def generate_random_map_custom(self, size, iceProb, slippery = False):
        if size <= 1:
            raise ValueError("El tamaño no puede ser 1")
        
        #Tamaño del entorno
        totalSize = size * size
        #Cantidad total de agujeros
        totalHole = round(totalSize * (1 - iceProb)) - 2
        #Se inicializa el entorno con F en todas las posiciones
        desc = [["F" for _ in range(0, size)] for _ in range(0, size)]
        #Se crea una lista con todas las posiciones del entorno (i, j)
        positions = [(i,j) for i in range(0, size) for j in range(0, size)]
        #Se mezcla la lista
        random.shuffle(positions)

        #Se obtiene una posición de la lista mezclada
        posStart = positions.pop()
        #En la posición obtenida se coloca la S
        desc[posStart[0]][posStart[1]] = "S"

        #Se obtiene otra posición de la lista mezclada
        posGoal = positions.pop()
        #En la posición obtenida se coloca la G
        desc[posGoal[0]][posGoal[1]] = "G"

        for i in range(0, totalHole):
            #Se obtiene otra posición de la lista mezclada
            posHole = positions.pop()
            #En la posición obtenida se coloca la H
            desc[posHole[0]][posHole[1]] = "H"
        env = gym.make("FrozenLake-v1", desc=desc, render_mode="human", is_slippery = slippery)
        return env, desc