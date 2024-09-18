import random
import math
# SimulatedAnnealing
def simulatedAnnealing(environment, limit):
    sol = environment.env
    cost = environment.cost
    costList = [cost]
    statesList = [1]
    states = 1
    T = 1

    while True:
        newSol = createNeighbour(sol)
        newCost = environment.h(newSol)
        
        if newCost == 0:
            sol = newSol
            cost = newCost
            costList.append(cost)
            statesList.append(states)
            break
        if newCost < cost:
            sol = newSol
            cost = newCost
            costList.append(cost)
            statesList.append(states)
        else:
            d = newCost - cost
            if random.random() < math.exp(-d / T):
                sol = newSol
                cost = newCost
                costList.append(cost)
                statesList.append(states)
        states += 1
        if states >= limit:
            break
        T = T * 0.99
        if T < 0.00001:
            break
    return sol, cost, states, costList, statesList

# Genera un vecino de la solución actual
def createNeighbour(solution):
    neighbour = solution.copy()
    n = len(solution)
    i = random.randint(0, n - 1)
    j = random.randint(0, n - 1)
    while j == solution[i]:
        j = random.randint(0, n - 1)
    neighbour[i] = j
    return neighbour