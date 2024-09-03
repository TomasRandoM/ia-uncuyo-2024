import agent
import environment
import random
import openpyxl
import time
import plot as plot


def addToExcel(name, n, states, cost1, cost2, time, solution):
    global row1
    global row2
    global row3
    global row4
    global row5
    global row6
    global row7
    row1.append(name)
    row2.append(n)
    row3.append(states)
    row4.append(cost1)
    row5.append(cost2)
    row6.append(time)
    row7.append(solution)


random.seed("TP3")
environmentList = []
for i in range(0, 30):
    environmentList.append(environment.Environment(100, 1-0.08))

agent = agent.Agent()

excelBook = openpyxl.Workbook()
#Se selecciona la hoja activa
sheet = excelBook.active
#Se colocan las etiquetas en la primera columna

row1 = ["algorithm_name"]
row2 = ["env_n"]
row3 = ["states_n"]
row4 = ["cost_e1"]
row5 = ["cost_e2"]
row6 = ["time"]
row7 = ["solution_found"]

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
    addToExcel("BFS", i + 1, len(path), len(directions), actions, executionTime, 1 if path != [] else 0)
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
    addToExcel("DFS", i + 1, len(path), len(directions), actions, executionTime, 1 if path != [] else 0)

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
    addToExcel("DLS", i + 1, len(path), len(directions), actions, executionTime, 1 if path != [] else 0)

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

    addToExcel("UCS_e1", i + 1, len(path), len(directions), "No aplica", executionTime, 1 if path != [] else 0)

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
    addToExcel("UCS_e2", i + 1, len(path), "No aplica", actions, executionTime, 1 if path != [] else 0)

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
    addToExcel("A*_e1", i + 1, len(path), len(directions), actions, executionTime, 1 if path != [] else 0)

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
    addToExcel("A*_e2", i + 1, len(path), len(directions), actions, executionTime, 1 if path != [] else 0)

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

sheet.append(row1)
sheet.append(row2)
sheet.append(row3)
sheet.append(row4)
sheet.append(row5)
sheet.append(row6)
sheet.append(row7)

#Se guarda el archivo excel.
excelBook.save("./results.csv")


plot.whiskers(generalTimeResults, "Execution Time", "Algorithm", "Time", "ExecutionTime")
plot.whiskers(generalExploredResults, "Explored States", "Algorithm", "States", "ExploredStates")
plot.whiskers(generalCost1Results, "Cost Scenary 1", "Algorithm", "Cost", "Cost1")
plot.whiskers(generalCost2Results, "Cost Scenary 2", "Algorithm", "Cost", "Cost2")



