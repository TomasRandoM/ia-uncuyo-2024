import matplotlib.pyplot as plot

def plotData(results, resultsRandom, dirtRate):
    #Se crea el gráfico de celdas limpiadas
    plot.figure(figsize=(10,6))
    environments =["2x2", "4x4", "8x8", "16x16", "32x32", "64x64", "128x128"]
    promCleaned, promMoved = getResults(results, dirtRate)
    promCleanedRandom, promMovedRandom = getResults(resultsRandom, dirtRate)

    for i in range(0, len(environments)):
        #Se colocan los puntos
        plot.scatter([i + 1], promCleaned[i], color="blue")
        plot.scatter([i + 1], promCleanedRandom[i], color="red")
        #Se colocan los valores en los puntos
        plot.text(i + 1, promCleaned[i], str(promCleaned[i]), ha='right', color='blue')
        plot.text(i + 1, promCleanedRandom[i], str(promCleanedRandom[i]), ha='right', color='red')

    #Se añaden las etiquetas a los valores del eje X
    plot.xticks(range(1, len(environments) + 1), environments)
    #Se añade el título
    plot.title("Celdas limpiadas por cada agente en cada entorno para el porcentaje de suciedad " + str(dirtRate))
    #Se añade el título del eje X
    plot.xlabel("Entornos")
    #Se añade el título del eje Y
    plot.ylabel("Celdas limpiadas")
    #Se hace visible la cuadrícula en el gráfico
    plot.grid(True)
    #Se guarda el gráfico
    plot.savefig("Cleaned" + str(dirtRate) + ".png")
    
    #Se crea el gráfico de movimientos realizados
    plot.figure(figsize=(10,6))
    for i in range(0, len(environments)):
        #Se colocan los puntos
        plot.scatter([i + 1], promMoved[i], color="blue")
        plot.scatter([i + 1], promMovedRandom[i], color="red")
        #Se colocan los valores en los puntos
        plot.text(i + 1, promMoved[i], str(promMoved[i]), ha='right', color='blue')
        plot.text(i + 1, promMovedRandom[i], str(promMovedRandom[i]), ha='right', color='red')

    #Se añaden las etiquetas a los valores del eje X
    plot.xticks(range(1, len(environments) + 1), environments)
    #Se añade el título
    plot.title("Movimientos realizados hasta limpiar todo por cada agente en cada entorno para el porcentaje de suciedad " + str(dirtRate))
    #Se añade el título del eje X
    plot.xlabel("Entornos")
    #Se añade el título del eje Y
    plot.ylabel("Movimientos")
    #Se hace visible la cuadrícula en el gráfico
    plot.grid(True)
    #Se guarda el gráfico
    plot.savefig("Moved" + str(dirtRate) + ".png")
    return 0

#Divide los resultados en dos listas, una del promedio de celdas limpiadas y otra del promedio de movimientos realizados. Ambos promedios correspondientes al dirtRate especificado.
def getResults(results, dirtRate):
    n = len(results)
    promCleaned = []
    promMoved = []
    for i in range(0, n):
        if results[i][1] == dirtRate:
            promCleaned.append(results[i][2])
            promMoved.append(results[i][3])
    return promCleaned, promMoved

#Hace el gráfico de cajas y extensiones, dataList1 y dataList2 son los datos (dataList2 puede ser None), title es el título del gráfico,
#ylabel es la etiqueta del eje y, xlabel es la etiqueta del eje x
def whiskers(dataList1, dataList2, title, ylabel, xlabel):
    plot.figure(figsize=(10, 6))
    plot.boxplot(dataList1, vert=False, patch_artist=True)
    if dataList2 != None:
        plot.boxplot(dataList2, vert=False, patch_artist=True)
    plot.title(title)
    plot.ylabel(ylabel)
    plot.xlabel(xlabel)
    plot.grid(True)
    plot.savefig("whiskers.png")
    return 0

    
