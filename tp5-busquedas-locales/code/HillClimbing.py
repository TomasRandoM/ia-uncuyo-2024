# Algoritmo Hill Climbing
def hillClimbing(environment, limit):
    sol = environment.env
    cost = environment.cost
    states = 1
    costList = [cost]
    while True:
        neighbours = createNeighboursList(sol)
        newSol, newCost = exploreNeighbours(environment, sol, cost, neighbours)
        if newCost == 0:
            break
        if newCost >= cost:
            break
        sol = newSol
        cost = newCost
        costList.append(cost)
        states += 1
        if states >= limit:
            break
    return newSol, newCost, states, costList

#Retorna la lista de vecinos de una solución
def createNeighboursList(solution):
    neighbours = []
    n = len(solution)
    for i in range(0, n):
        for j in range(0, n):
            if solution[i] != j:
                neighbour = solution.copy()
                neighbour[i] = j
                neighbours.append(neighbour)
    return neighbours

#Explora los vecinos de una solución y retorna la mejor solución y su costo
def exploreNeighbours(environment, solution, cost, neighbours):
    m = len(neighbours)
    actSolution = solution
    actCost = cost
    for i in range(0, m):
        newCost = environment.h(neighbours[i])

        if newCost < actCost:
            actCost = newCost
            actSolution = neighbours[i]

    return actSolution, actCost