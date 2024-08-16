import agent
import random

class RandomAgent(agent.Agent):
    def __init__(self, env):
        super().__init__(env)

    #Verifica si tiene movimientos restantes
    def detention(self):
        if self.lives == 0:
            return True
        else:
            return False
    
    #Implementa el proceso que realiza el agente
    def think(self):
        while not self.detention():
            actionNumber = random.randint(0, 5)
            if actionNumber == 0:
                self.up()
            elif actionNumber == 1:
                self.down()
            elif actionNumber == 2:
                self.left()
            elif actionNumber == 3:
                self.right()
            elif actionNumber == 4:
                execution = self.suck()
                if execution == True:
                    self.cleaned += 1
            else:
                self.idle()
            self.lives -= 1
        return self.cleaned