import HillClimbing
import SimulatedAnnealing
import Environment
import random
import time
import plot
import csv

def generateEnvironments():
    n = [4, 8, 10, 12, 15]
    environments = []
    for j in n:
        for i in range(0, 30):
            env = Environment.Environment(j)
            environments.append((env))
    return environments

if __name__ == "__main__":
    random.seed("TP5")
    
    envList = generateEnvironments()
    

    hcResults = []
    hcCostTimeStates = [[0], [], []]
    saResults = []
    saCostTimeStates = [[0], [], []]
    costLists = []
    saStateList = []
    count = 0
    for i in range(0, len(envList)):
        count += 1
        start = time.time()
        sol, cost, states, costList = HillClimbing.hillClimbing(envList[i], 5000)
        end = time.time()
        hcCostTimeStates[0][len(hcCostTimeStates[0]) - 1] = hcCostTimeStates[0][len(hcCostTimeStates[0]) - 1] + cost
        hcCostTimeStates[1].append(end - start)
        hcCostTimeStates[2].append(states)
        hcResults.append(["HillClimbing", envList[i].n,  sol, cost, states, end - start])

        start = time.time()
        sol, cost, states, costList2, statesList = SimulatedAnnealing.simulatedAnnealing(envList[i], 5000)
        end = time.time()
        saCostTimeStates[0][len(saCostTimeStates[0]) - 1] = saCostTimeStates[0][len(saCostTimeStates[0]) - 1] + cost
        saCostTimeStates[1].append(end - start)
        saCostTimeStates[2].append(states)
        saResults.append(["SimulatedAnnealing", envList[i].n, sol, cost, states, end - start])
        if count == 30:
            count = 0
            saCostTimeStates[0][len(saCostTimeStates[0]) - 1] = saCostTimeStates[0][len(saCostTimeStates[0]) - 1] / 30
            hcCostTimeStates[0][len(hcCostTimeStates[0]) - 1] = hcCostTimeStates[0][len(hcCostTimeStates[0]) - 1] / 30
            if envList[i].n != 15:
                saCostTimeStates[0].append(0)
                hcCostTimeStates[0].append(0)

        if costLists == [] and envList[i].n == 8:
            costLists.append(costList)
            costLists.append(costList2)
            saStateList = statesList


    plot.plotData(costLists[0], "HillClimbingH", [i for i in range(1, len(costLists[0]) + 1)], "Función H para Hill Climbing con n = 8", "Iteración", "Costo", 10, 6)
    plot.plotData(costLists[1], "SimulatedAnnealingH", saStateList, "Función H para Simulated Annealing con n = 8", "Iteración", "Costo", 35, 15)
    plot.plotData(hcCostTimeStates[0], "HillClimbingCosts", [4, 8, 10, 12, 15], "Costo promedio de Hill Climbing para cada environment", "n", "Costo", 10, 6)
    plot.plotData(saCostTimeStates[0], "SimulatedAnnealingCosts", [4, 8, 10, 12, 15], "Costo promedio de Simulated Annealing para cada environment", "n", "Costo", 10, 6)
    plot.whiskers([hcCostTimeStates[1], saCostTimeStates[1]], "Execution Time", "Algorithm", "Tiempo de ejecución", "ExecutionTime", ["HillClimbing", "SimulatedAnnealing"])
    plot.whiskers([hcCostTimeStates[2], saCostTimeStates[2]], "States", "Algorithm", "Estados", "States", ["HillClimbing", "SimulatedAnnealing"])

    # Escribir los resultados en un archivo CSV
    filename = "./results.csv"
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        
        # Escribir cada fila en el archivo CSV
        writer.writerow(["Algorithm_name", "Environment size", "Solution", "Cost", "States", "Time"])
        for row in hcResults:
            writer.writerow(row)
        for row in saResults:
            writer.writerow(row)