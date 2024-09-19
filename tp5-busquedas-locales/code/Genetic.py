import random

def generatePopulation(n, size):
    return [[random.randint(0, size - 1) for _ in range(size)] for _ in range(n)]

def selection(env, population, k):
    bestRes = []
    bestCost = None
    sizePop = len(population)
    for i in range(0, k):
        sel = random.randint(0, sizePop - 1)
        if bestRes == []:
            bestRes = population[sel]
            bestCost = env.h(bestRes)
        else:
            newRes = population[sel]
            newCost = env.h(newRes)
            if newCost <= bestCost:
                bestRes = newRes
                bestCost = newCost
    return bestRes

def crossover(parent1, parent2):
    point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:point] + parent2[point:]
    return child1
        
def mutate(solution):
    if 0.1 < random.random():
        return solution
    column = random.randint(0, len(solution) - 1)
    newValue = random.randint(0, len(solution) - 1)
    while newValue == solution[column]:
        newValue = random.randint(0, len(solution) - 1)
    solution[column] = newValue
    return solution
        
def genetic(env, m, limit):
    actualSol = env.env
    size = env.n
    actualCost = env.h(actualSol)
    generationCostList = [actualCost]
    listIter = [1]
    population = generatePopulation(m, size)
    generations = 1
    costList = [actualCost]
    iter = 1
    
    while True:
        nextGenPopulation = []
        for i in range(0, len(population)):
            st1 = selection(env, population, 10)
            st2 = selection(env, population, 10)
            iter += 1
            child = crossover(st1, st2)
            child = mutate(child)
            childCost = env.h(child)
            if childCost < actualCost:
                actualSol = child
                actualCost = childCost
                costList.append(actualCost)
                listIter.append(iter)
            nextGenPopulation.append(child)
        generations += 1
        generationCostList.append(actualCost)
        if generations >= limit:
            break
        if actualCost == 0:
            break
        population = nextGenPopulation
    return actualSol, actualCost, generations, listIter, costList, generationCostList
        
                
        
        
