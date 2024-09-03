import agent
import environment
import random
import csv
import time
import plot as plot



random.seed("TP3")
environmentList = []
for i in range(0, 30):
    environmentList.append(environment.Environment(100, 1-0.08))

agent = agent.Agent()


rows = [["algorithm_name", "env_n", "states_n", "cost_e1", "cost_e2", "time", "solution_found"]]


resultsState = []
resultsDirections = []

generalTimeResults = []
generalExploredResults = []
generalCost1Results = []
generalCost2Results = []

timeResults = []
exploredResults = []
cost1Results = []
cost2Results = []
for i in range(0, 30):
    start = time.time()
    path, directions, explorados = agent.recorrerAnchura(environmentList[i])
    end = time.time()
    executionTime = end - start
    actions = agent.countActions(directions)
    rows.append(["BFS", i + 1, len(path), len(directions), actions, executionTime, 1 if path != [] else 0])
    resultsState.append(path)
    resultsDirections.append(directions)
    if path != []:
        timeResults.append(executionTime)
        exploredResults.append(len(explorados))
        if len(directions) <= 1000:
            cost1Results.append(len(directions))
        if actions <= 1000:
            cost2Results.append(actions)

generalCost1Results.append(cost1Results)
generalCost2Results.append(cost2Results)
generalTimeResults.append(timeResults)
generalExploredResults.append(exploredResults)


timeResults = []
exploredResults = []
cost1Results = []
cost2Results = []
for i in range(0, 30):
    start = time.time()
    path, directions, explorados = agent.recorrerProfundidad(environmentList[i])
    end = time.time()
    executionTime = end - start

    actions = agent.countActions(directions)
    rows.append(["DFS", i + 1, len(path), len(directions), actions, executionTime, 1 if path != [] else 0])
    resultsState.append(path)
    resultsDirections.append(directions)

    if path != []:
        timeResults.append(executionTime)
        exploredResults.append(len(explorados))
        if len(directions) <= 1000:
            cost1Results.append(len(directions))
        if actions <= 1000:
            cost2Results.append(actions)

generalCost1Results.append(cost1Results)
generalCost2Results.append(cost2Results)
generalTimeResults.append(timeResults)
generalExploredResults.append(exploredResults)


timeResults = []
exploredResults = []
cost1Results = []
cost2Results = []
for i in range(0, 30):
    start = time.time()
    path, directions, explorados = agent.recorrerProfundidadLimitada(environmentList[i], 10)
    end = time.time()
    executionTime = end - start
    actions = agent.countActions(directions)
    rows.append(["DLS", i + 1, len(path), len(directions), actions, executionTime, 1 if path != [] else 0])

    resultsState.append(path)
    resultsDirections.append(directions)

    if path != []:
        timeResults.append(executionTime)
        exploredResults.append(len(explorados))
        if len(directions) <= 1000:
            cost1Results.append(len(directions))
        if actions <= 1000:
            cost2Results.append(actions)

generalCost1Results.append(cost1Results)
generalCost2Results.append(cost2Results)
generalTimeResults.append(timeResults)
generalExploredResults.append(exploredResults)


timeResults = []
exploredResults = []
cost1Results = []
cost2Results = []
for i in range(0, 30):
    start = time.time()
    path, directions, explorados = agent.recorrerCostoUniforme(environmentList[i], 1)
    end = time.time()
    executionTime = end - start

    rows.append(["UCS_e1", i + 1, len(path), len(directions), "No aplica", executionTime, 1 if path != [] else 0])

    resultsState.append(path)
    resultsDirections.append(directions)

    if path != []:
        timeResults.append(executionTime)
        exploredResults.append(len(explorados))
        if len(directions) <= 1000:
            cost1Results.append(len(directions))
        if actions <= 1000:
            cost2Results.append(actions)

generalCost1Results.append(cost1Results)
generalCost2Results.append(cost2Results)
generalTimeResults.append(timeResults)
generalExploredResults.append(exploredResults)



timeResults = []
exploredResults = []
cost1Results = []
cost2Results = []
for i in range(0, 30):
    start = time.time()
    path, directions, explorados = agent.recorrerCostoUniforme(environmentList[i], 2)
    end = time.time()
    executionTime = end - start
    actions = agent.countActions(directions)
    rows.append(["UCS_e2", i + 1, len(path), "No aplica", actions, executionTime, 1 if path != [] else 0])

    resultsState.append(path)
    resultsDirections.append(directions)

    if path != []:
        timeResults.append(executionTime)
        exploredResults.append(len(explorados))
        if len(directions) <= 1000:
            cost1Results.append(len(directions))
        if actions <= 1000:
            cost2Results.append(actions)

generalCost1Results.append(cost1Results)
generalCost2Results.append(cost2Results)
generalTimeResults.append(timeResults)
generalExploredResults.append(exploredResults)



timeResults = []
exploredResults = []
cost1Results = []
cost2Results = []
for i in range(0, 30):
    start = time.time()
    path, directions, explorados = agent.aEstrella(environmentList[i], 1)
    end = time.time()
    executionTime = end - start
    actions = agent.countActions(directions)
    rows.append(["A*_e1", i + 1, len(path), len(directions), actions, executionTime, 1 if path != [] else 0])

    resultsState.append(path)
    resultsDirections.append(directions)

    if path != []:
        timeResults.append(executionTime)
        exploredResults.append(len(explorados))
        if len(directions) <= 1000:
            cost1Results.append(len(directions))
        if actions <= 1000:
            cost2Results.append(actions)

generalCost1Results.append(cost1Results)
generalCost2Results.append(cost2Results)
generalTimeResults.append(timeResults)
generalExploredResults.append(exploredResults)


timeResults = []
exploredResults = []
cost1Results = []
cost2Results = []
for i in range(0, 30):
    start = time.time()
    path, directions, explorados = agent.aEstrella(environmentList[i], 2)
    end = time.time()
    executionTime = end - start
    actions = agent.countActions(directions)
    rows.append(["A*_e2", i + 1, len(path), len(directions), actions, executionTime, 1 if path != [] else 0])

    if path != []:
        timeResults.append(executionTime)
        exploredResults.append(len(explorados))
        if len(directions) <= 1000:
            cost1Results.append(len(directions))
        if actions <= 1000:
            cost2Results.append(actions)

generalCost1Results.append(cost1Results)
generalCost2Results.append(cost2Results)
generalTimeResults.append(timeResults)
generalExploredResults.append(exploredResults)

filename = "results.csv"
with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    
    # Escribir cada fila en el archivo CSV
    for row in rows:
        writer.writerow(row)

plot.whiskers(generalTimeResults, "Execution Time", "Algorithm", "Time", "ExecutionTime")
plot.whiskers(generalExploredResults, "Explored States", "Algorithm", "States", "ExploredStates")
plot.whiskers(generalCost1Results, "Cost Scenary 1", "Algorithm", "Cost", "Cost1")
plot.whiskers(generalCost2Results, "Cost Scenary 2", "Algorithm", "Cost", "Cost2")



