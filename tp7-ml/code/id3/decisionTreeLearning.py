import pandas
import numpy

#Se implementó tomando en cuenta el pseudocódigo del AIMA y las fórmulas de entropía e information gain de la sección 18.3.4 del mismo libro

#Se devuelve el atributo más frecuente
def pluralityValue(data, target):
    return data[target].mode()[0]

# Se calcula la entropía de una columna utilizando la fórmula disponible en el AIMA
def entropy(column):
    n = len(column)
    values = column.value_counts()
    entropy = 0
    for i in values:
        p = i/n
        entropy += -p * numpy.log2(p)
    return entropy

# Se calcula el information gain con la fórmula en cuestión
def calculateEntropy(examples, attribute, target):
    # Se calcula la entropía anterior
    entropyBefore = entropy(examples[target])
    # Se obtiene cada valor único de la columna
    dataList = examples[attribute].unique()

    # Se itera sobre cada valor
    for i in range(0, len(dataList)):
        #Se obtienen las filas que contienen el valor de la iteración
        auxiliar = examples[examples[attribute] == dataList[i]]
        # Se calcula la entropía posterior utilzando la fórmula
        entropyAfter = (len(auxiliar) / len(examples)) * entropy(auxiliar[target])
    # Se calcula el information gain
    result = entropyBefore - entropyAfter
    return result

#Se implementa la función importance del AIMA
def importance(examples, attributes, target):
    auxList = []
    # Calcula el information gain de cada atributo y el que posee mayor es el retornado
    mostImportant = (attributes[0], calculateEntropy(examples, attributes[0], target))
    for i in range(1, len(attributes)):
        aux = calculateEntropy(examples, attributes[i], target)
        if aux > mostImportant[1]:
            mostImportant = (attributes[i], aux)
    return mostImportant[0]

# Se implementa el algoritmo ID3 del AIMA utilizando el respectivo pseudocódigo     
def decisionTreeLearning(examples, attributes, parent_examples, target):
    if examples.empty:
        return pluralityValue(parent_examples, target)
    
    if len(examples[target].unique()) == 1:
        return examples[target].iloc[0]

    if len(attributes) == 0:
        return pluralityValue(examples, target)
    
    # Se obtiene el atributo más importante y se crea el nodo raíz
    A = importance(examples, attributes, target)
    tree = {A: {}}

    # Se obtienen los valores únicos del atributo más importante
    valuesOfA = examples[A].unique()
    # Se elimina el atributo de la lista de atributos
    attributes.remove(A)
    # Se itera sobre cada valor
    for i in valuesOfA:
        # Se obtienen las filas que contienen el valor de la iteración
        exs = examples[examples[A] == i]
        # Se llama recursivamente a la función para obtener un subárbol
        subtree = decisionTreeLearning(exs, attributes, examples, target)
        # Se añade el subárbol al árbol
        tree[A][i] = subtree
    return tree