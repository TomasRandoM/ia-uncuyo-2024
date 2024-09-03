import agent
import environment
import random
import gymnasium as gym
import csv
import time
import plot as plot
import tkinter

#Función para ejecutar los resultados en todos los entornos y ser mostrados en pantalla. Se ejecuta cuando se presiona el botón
def executeAllResults(envList, direc, window):
    window.destroy()
    algorithmList = ["BFS", "DFS", "DLS", "UCS_e1", "UCS_e2", "A*_e1", "A*_e2"]
    n = len(direc)
    count = 0
    count2 = 0
    algo = algorithmList.pop(0)
    for i in range(0, n):
        count2 = count2 + 1
        if count2 == 31:
            algo = algorithmList.pop(0)
            count2 = 1
        
        print("===== Entorno ", count2, " with algorithm ", algo, "======")
        env = envList[count].env
        direcciones = direc[i]
        if direcciones == []:
            print("No se alcanzó el objetivo en este entorno con este algoritmo")
            j = j + 1
            if count == 29:
                count = 0
            else:
                count = count + 1
            continue
        state = env.reset()
        print("Posición inicial del agente:", state[0])

        done = truncated = False
        env.render()
        j = 0

        while not (done or truncated):
            #Acción aleatoria
            action = direcciones[j]
            next_state, reward, done, truncated, _ = env.step(action)
            if done == True or truncated == True:
                print(f"Acción: {action}, Nuevo estado: {next_state}, Recompensa: {reward}")
                print(f"¿Ganó? (encontró el objetivo): {done}")
                print(f"¿Frenó? (alcanzó el máximo de pasos posible): {truncated}\n")
            state = next_state
            if j == len(direcciones) - 1:
                break
            j += 1
        if count == 29:
            count = 0
        else:
            count += 1
    exit(0)

#Función para mostrar los entornos cuando se presiona el botón
def showEnvironment(envList, window):
    window.destroy()
    for i in range(0, len(envList)):
        env = envList[i].env
        env.reset()
        env.render()
        time.sleep(3)
    exit(0)

#Función para cerrar la ventana cuando se presiona el botón de salir
def destroyWindow(window):
    window.destroy()
    exit(0)

#Función para obtener los resultados de los algoritmos en los entornos
def getResults(algorithm, algorithmName , envList):
    global rows
    global resultsState
    global resultsDirections
    global generalTimeResults
    global generalExploredResults
    global generalCost1Results
    global generalCost2Results
    global generalCountSolutionFound

    #Listas para guardar los resultados de cada algoritmo
    timeResults = []
    exploredResults = []
    cost1Results = []
    cost2Results = []
    countSolutionFound = 0
    for i in range(0, 30):
        start = time.time()
        #Se ejecuta el algoritmo
        if algorithmName == "UCS_e1" or algorithmName == "A*_e1":
            path, directions, explorados = algorithm(envList[i], 1)
        elif algorithmName == "UCS_e2" or algorithmName == "A*_e2":
            path, directions, explorados = algorithm(envList[i], 2)
        elif algorithmName == "DLS":
            path, directions, explorados = algorithm(envList[i], 10)
        else: 
            path, directions, explorados = algorithm(environmentList[i])
        end = time.time()
        executionTime = end - start
        #Se cuentan las acciones con costo personalizado
        actions = agent.countActions(directions)
        #Se añaden los resultados a la lista
        if algorithmName == "UCS_e1":
            rows.append([algorithmName, i + 1, len(path), len(directions), "No aplica", executionTime, 1 if path != [] else 0])
        elif algorithmName == "UCS_e2":
            rows.append([algorithmName, i + 1, len(path), "No aplica", actions, executionTime, 1 if path != [] else 0])
        else:
            rows.append([algorithmName, i + 1, len(path), len(directions), actions, executionTime, 1 if path != [] else 0])
        resultsState.append(path)
        resultsDirections.append(directions)
        timeResults.append(executionTime)
        if path != []:
            exploredResults.append(len(explorados))
            if len(directions) <= 1000:
                if algorithmName != "UCS_e2" and algorithmName != "A*_e2":
                    cost1Results.append(len(directions))
                    countSolutionFound += 1
            if actions <= 1000:
                if algorithmName != "UCS_e1" and algorithmName != "A*_e1":
                    cost2Results.append(actions)
                if algorithmName == "UCS_e2" or algorithmName == "A*_e2":
                    countSolutionFound += 1
    #Se añaden los resultados a las listas generales
    generalCost1Results.append(cost1Results)
    generalCost2Results.append(cost2Results)
    generalTimeResults.append(timeResults)
    generalExploredResults.append(exploredResults)
    generalCountSolutionFound.append(countSolutionFound)

if __name__ == "__main__":
    #Se fija la semilla para que los resultados sean reproducibles
    random.seed("TP3")
    #Se crea la lista de entornos
    environmentList = []
    for i in range(0, 30):
        #Se crea el entorno
        environmentList.append(environment.Environment(100, 1-0.08))

    #Se crea el agente
    agent = agent.Agent()

    #Se crea la lista de resultados que será utilizada para guardar los resultados en un archivo CSV
    rows = [["algorithm_name", "env_n", "states_n", "cost_e1", "cost_e2", "time", "solution_found"]]

    #Listas para guardar los resultados generales
    resultsState = []
    resultsDirections = []
    generalTimeResults = []
    generalExploredResults = []
    generalCost1Results = []
    generalCost2Results = []
    generalCountSolutionFound = []

    getResults(agent.recorrerAnchura, "BFS", environmentList)
    getResults(agent.recorrerProfundidad, "DFS", environmentList)
    getResults(agent.recorrerProfundidadLimitada, "DLS", environmentList)
    getResults(agent.recorrerCostoUniforme, "UCS_e1", environmentList)
    getResults(agent.recorrerCostoUniforme, "UCS_e2", environmentList)
    getResults(agent.aEstrella, "A*_e1", environmentList)
    getResults(agent.aEstrella, "A*_e2", environmentList)
    getResults(agent.recorrerAleatorio, "Random", environmentList)

    # Escribir los resultados en un archivo CSV
    filename = "./results.csv"
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        
        # Escribir cada fila en el archivo CSV
        for row in rows:
            writer.writerow(row)

    # Graficar los resultados
    plot.whiskers(generalTimeResults, "Execution Time", "Algorithm", "Time", "ExecutionTime")
    plot.whiskers(generalExploredResults, "Explored States", "Algorithm", "States", "ExploredStates")
    plot.whiskers(generalCost1Results, "Cost Scenary 1", "Algorithm", "Cost", "Cost1")
    plot.whiskers(generalCost2Results, "Cost Scenary 2", "Algorithm", "Cost", "Cost2")
    plot.plotData(generalCountSolutionFound, "SolutionFound")

    """
    # Crear la ventana principal
    window = tkinter.Tk()
    # Colocar el título de la ventana
    window.title("Opciones")
    # Tamaño de la ventana
    window.geometry("500x50")  # Tamaño de la ventana

    # Crear y posicionar los botones en la ventana
    boton1 = tkinter.Button(window, text="Mostrar escenarios", command= lambda: showEnvironment(environmentList, window))
    boton1.pack(side=tkinter.LEFT, padx=10, pady=5)

    boton2 = tkinter.Button(window, text="Ejecutar resultados en TODOS los escenarios", command= lambda: executeAllResults(environmentList, resultsDirections, window))
    boton2.pack(side=tkinter.RIGHT, padx=5, pady=5)

    boton3 = tkinter.Button(window, text="Salir", command= lambda: destroyWindow(window))
    boton3.pack(side=tkinter.BOTTOM, padx=2, pady=10)

    window.mainloop()
    """