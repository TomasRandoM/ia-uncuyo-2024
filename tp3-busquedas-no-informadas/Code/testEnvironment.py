#Se realiza la parte del práctico que tiene que ver con la exploración del entorno
import random
import gymnasium as gym
from gymnasium.envs.toy_text.frozen_lake import generate_random_map
from gymnasium import wrappers

#Crear entorno por defecto
env = gym.make("FrozenLake-v1", render_mode="human")

#Obtener información del entorno
print("Número de estados:", env.observation_space.n)
print("Número de acciones:", env.action_space.n)


#Episodio básico

state = env.reset()
print("Posición inicial del agente:", state[0])

done = truncated = False
env.render()
while not (done or truncated):
    #Acción aleatoria
    action = env.action_space.sample()
    next_state, reward, done, truncated, _ = env.step(action)
    print(f"Acción: {action}, Nuevo estado: {next_state}, Recompensa: {reward}")
    print(f"¿Ganó? (encontró el objetivo): {done}")
    print(f"¿Frenó? (alcanzó el máximo de pasos posible): {truncated}\n")
    state = next_state


#4
#a) is_slippery controla la dirección en la que se mueve el jugador. Es decir, si es = True, el jugador
#se moverá en la dirección correcta 1/3 de las veces, el resto de las veces se moverá hacia alguno de los
#dos lados perpendiculares con probabilidad 1/3 en cada dirección. El valor por defecto es True

gym.make("FrozenLake-v1", desc=None, map_name="4x4", render_mode="human")


#b)

#Se define el entorno manualmente
#S es start, F es Free Space, H es Hole y G es Goal 
desc=["SFFF", "FHFH", "FFFH", "HFFG"]
#Es de 4x4, tiene 4 agujeros, se comienza en la esquina superior izquierda y la recompensa está en la esquina inferior derecha
newEnv = gym.make("FrozenLake-v1", desc=desc, render_mode="human")
newEnv.reset()
newEnv.render()

#Genera entornos random de 8x8 con distintas cantidades de agujeros. Siempre se comienza en la esquina superior izquierda y
#la recompensa se encuentra en la esquina inferior derecha
newEnv = gym.make("FrozenLake-v1", desc=generate_random_map(size=8), render_mode="human")
newEnv.reset()
newEnv.render()


#c)
def generate_random_map_custom(size, iceProb, slippery = False):
    if size <= 1:
        return False
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
    return env

random.seed("BlueSky")
newEnv = generate_random_map_custom(8, 0.8)
newEnv.reset()
newEnv.render()

#Modificar la vida del agente
new_limit = 10
env = gym.make("FrozenLake-v1", render_mode="human").env
env = wrappers.TimeLimit(env, new_limit)
