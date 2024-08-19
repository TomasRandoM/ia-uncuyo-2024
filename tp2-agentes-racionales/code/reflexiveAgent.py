import agent
import random

class ReflexiveAgent(agent.Agent):
    def __init__(self, env):
        super().__init__(env)

    #Verifica el entorno con su sensor (Verifica si está limpia la casilla actual)
    def perspective(self):
        return self.env.isDirty(self.posX, self.posY)

    #Verifica si tiene movimientos restantes
    def detention(self):
        if self.lives == 0:
            return True
        else:
            return False
    
    #Implementa el proceso que realiza el agente
    def think(self):
        #Variable solo utilizada para medir el performance
        if self.env.dirt == 0:
            movesMade = 0
        else:
            movesMade = 1000
        while not self.detention():
            if self.perspective() == True:
                self.suck()
                self.cleaned += 1

                if self.env.dirt == 0:
                    movesMade = movesMade - self.lives
            else:
                actionNumber = random.randint(0, 3)
                if actionNumber == 0:
                    self.up()
                elif actionNumber == 1:
                    self.down()
                elif actionNumber == 2:
                    self.left()
                elif actionNumber == 3:
                    self.right()
            self.lives -= 1
        return self.cleaned, movesMade
