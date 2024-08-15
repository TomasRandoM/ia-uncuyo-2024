from environment import * 
import random

class Agent:
    def __init__(self, env):
        posX = random.randint(0, env.sizeX - 1)
        posY = random.randint(0, env.sizeY - 1)
        #Casillas limpiadas
        cleaned = 0
        #Tiempo de vida restante
        lives = 1000
    
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
        if self.env.acceptAction("Limpiar", self.posX, self.posY) == True:
            cleaned = cleaned + 1
        return
    
    #No realiza ninguna acción
    def idle(self):
        return
    
    #Sensa el entorno
    def perspective(self):
        #Pendiente de implementación
        return
    
    #Implementa las acciones que realizará el agente
    def think(self):
        #Pendiente de implementación
        return