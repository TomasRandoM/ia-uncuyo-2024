import pandas
import decisionTreeLearning

#Imprime el árbol 
def print_tree(tree, indent=""):
    if isinstance(tree, dict):
        #Se iera sobre los atributos y valores
        for attribute, branches in tree.items():
            print(indent + str(attribute))
            #Nuevamente se itera sobre los atributos y valores pero ahora del subárbol
            for value, subtree in branches.items():
                print(indent + "  └── " + str(value))
                #Se llama recursivamente a la función para imprimir el subárbol con mayor indentación
                print_tree(subtree, indent + "      ")
    else:
        #Si no es un diccionario, significa que no se encontró un subárbol, por ello, debemos estar en un nodo hoja. Entonces, se imprime por pantalla
        print(indent + "  └── " + str(tree))

if __name__ == "__main__":
    csv = pandas.read_csv("https://raw.githubusercontent.com/sjwhitworth/golearn/master/examples/datasets/tennis.csv")

    attributes = list(csv.columns)
    attributes.remove("play")
    target = "play"

    tree = decisionTreeLearning.decisionTreeLearning(csv, attributes, csv, target)
    print_tree(tree)