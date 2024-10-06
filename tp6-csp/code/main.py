import CSPBacktracking
import CSPForwardChecking
import plot
import time
import csv

#Calcula los ataques entre reinas
def attacksAuxiliar(env):
        attacks = 0
        m = len(env)
        for i in range(0, m):
            for j in range(i + 1, m):
                if env[i] == env[j] or abs(env[j] - env[i]) == abs(j - i):
                    attacks += 1
        return attacks

if __name__ == "__main__":
    n = [4, 8, 10, 12, 15]
    resultsB = []
    resultsF = []
    index = 0
    optim = [0] * 5
    optim2 = [0] * 5
    for i in n:
        for _ in range(0, 30):
            cspBack = CSPBacktracking.CSPBacktracking(i);
            start = time.time()
            solution = cspBack.solveCsp()
            end = time.time()
            resultsB.append(["CSP Backtracking", solution, cspBack.iteration, end - start])

            cspForward = CSPForwardChecking.CSPForwardChecking(i);
            start = time.time()
            solution = cspForward.solveCsp()
            end = time.time()
            resultsF.append(["CSP Forward Checking", solution, cspForward.iteration, end - start])

            if attacksAuxiliar(cspBack.actualSolution) == 0:
                optim[index] += 1
            if attacksAuxiliar(cspForward.actualSolution) == 0:
                optim2[index] += 1
        optim[index] = optim[index] / 30
        optim2[index] = optim2[index] / 30
        index += 1

    resultsTime = [[], []]
    resultsStates = [[], []]
    
    count = 0
    for i in range(0, len(resultsB)):
        resultsTime[0].append(resultsB[i][3])
        resultsTime[1].append(resultsF[i][3])
        # resultsStates[0].append(resultsB[i][2])
        # resultsStates[1].append(resultsF[i][2])
        if count == 0:
            resultsStates[0].append(resultsB[i][2])
            resultsStates[1].append(resultsF[i][2])
            count += 1
        elif count == 29:
            count = 0
        else:
            count += 1

    plot.whiskers(resultsTime, "Execution Time", "Algorithm", "Time", "ExecutionTime", ["CSP Backtracking", "CSP ForwardChecking"])
    # plot.whiskers(resultsStates, "Iterations", "Algorithm", "Iterations", "Iterations", ["CSP Backtracking", "CSP ForwardChecking"])
    plot.plotData(optim, "OptimalWithBacktracking", n, "Percentage of optimal solutions with CSPBacktracking", "Size", "Optimal Solutions", 10, 6)
    plot.plotData(optim2, "OptimalWithForwardChecking", n, "Percentage of optimal solutions with CSPForwardChecking", "Size", "Optimal Solutions", 10, 6)
    plot.plotData(resultsStates[0], "StatesWithBacktracking", n, "States visited with CSPBacktracking", "Environment size", "States", 10, 6)
    plot.plotData(resultsStates[1], "StatesWithForwardChecking", n, "States visited with CSPForwardChecking", "Environment size", "States", 10, 6)
    # Escribir los resultados en un archivo CSV
    filename = "./tp6-Nreinas.csv"
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        
        # Escribir cada fila en el archivo CSV
        writer.writerow(["Algorithm name", "Solution", "Iterations", "Time"])
        for row in resultsB:
            writer.writerow(row)
        for row in resultsF:
            writer.writerow(row)

    filename = "./percentageTable.csv"
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        
        # Escribir cada fila en el archivo CSV
        writer.writerow(["Algorithm name", "Size", "Percentage"])
        for i in range(0, len(n)):
            rowA = ["CSP Backtracking", n[i], optim[i]]
            writer.writerow(rowA)
        for i in range(0, len(n)):
            rowA = ["CSP Forward Checking", n[i], optim2[i]]
            writer.writerow(rowA)