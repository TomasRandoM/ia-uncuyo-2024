from abc import ABC, abstractmethod
from environment import * 
import random

class Agent(ABC):
    def __init__(self, env):
        self.posX = random.randint(0, env.sizeX - 1)
        self.posY = random.randint(0, env.sizeY - 1)
        #Casillas limpiadas
        self.cleaned = 0
        self.env = env
        #Tiempo de vida restante
        self.lives = 1000
    
    #Se mueve hacia arriba
    def up(self):
        if self.env.acceptAction("Arriba", self.posX, self.posY) == True:
            self.posX = self.posX + 1
        return
    
    #Se mueve hacia abajo
    def down(self):
        if self.env.acceptAction("Abajo", self.posX, self.posY) == True:
            self.posX = self.posX - 1
        return
    
    #Se mueve hacia la izquierda
    def left(self):
        if self.env.acceptAction("Izquierda", self.posX, self.posY) == True:
            self.posY = self.posY - 1
        return
    
    #Se mueve hacia la derecha
    def right(self):
        if self.env.acceptAction("Derecha", self.posX, self.posY) == True:
            self.posY = self.posY + 1
        return
    
    #Limpia la casilla actual
    def suck(self):
        return self.env.acceptAction("Limpiar", self.posX, self.posY)
    
    #No realiza ninguna acción
    def idle(self):
        return
    
    #Implementa las acciones que realizará el agente
    @abstractmethod
    def think(self):
        return