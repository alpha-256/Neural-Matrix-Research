
from random import randint
from random import choice


def createBaseMatrix(layerCount, matrixSize):

    # Generate layers
    pathMatrix = []
    for layer in range(layerCount):
        tempArray = []
        for n in range(matrixSize):
            cellType = choice(["G", "R"])
            tempArray.append(cellType)
        pathMatrix.append(tempArray)

    return pathMatrix

def createOutputCells(pathMatrix, oAmount=3):

    # For each layer, randomly select 3 position for "O"
    # Note: The position can overlap
    for layer in pathMatrix:
        for n in range(oAmount):
            # Randomly choose an index
            randomIndex = randint(0, len(layer)-1)
            # Change element at index
            layer[randomIndex] = "O"

    return

def createInputCells(pathMatrix):

    # Randomly insert "I" in the 1st layer (index 0 layer)
    randomIndex = randint(0, len(pathMatrix[0])-1)
    pathMatrix[0][randomIndex] = "I"

    return

def connectIOCells(pathMatrix):

    # Start from the 2nd layer (Index of 1)
    # loop through elements of the previous layer (matrix_idx - 1)
    for layer, currentLayer in enumerate(pathMatrix[1:], start=1):
        previousLayer = pathMatrix[layer-1]
        for element, cellType in enumerate(previousLayer):

            # If "O" is found, replace the current layer of the same
            # index with "I"
            if cellType == "O":
                currentLayer[element] = "I"

    return

def print_all_layers(pathMatrix, size):

    # For printing the layers
    for layer in pathMatrix:
        for index, element in enumerate(layer):
            if index % size == 0:
                print()
            print(element, end=" ")
        print()

    return

layerCount = None
size = None
ruleMatrix = None

def _main():
    global layerCount
    global size
    layerCount = int(input("Layer count > "))
    size = int(input("Size > "))

    global ruleMatrix
    ruleMatrix = createBaseMatrix(layerCount, size*size)
    createOutputCells(ruleMatrix, 3)
    createInputCells(ruleMatrix)

    print("Generated Layer")
    print_all_layers(ruleMatrix, size)
    print("---")

    connectIOCells(ruleMatrix)

    print("Connected Layer")
    print_all_layers(ruleMatrix, size)
    print("---")

if __name__ == "__main__":
    _main()
