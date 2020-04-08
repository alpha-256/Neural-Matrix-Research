from random import randint as ri
from random import choice as rc
from pprint import pprint

neuralMatrix = []
rowIOLog = []
columnIOLog = []
cellTypes = ["I", "O"]
pathTypeCells = ["G", "R"]
"""
I = input   Cell
O = Output  Cell
G = Green   Cell    (Increase signal per step from I Cell)
R = Red     Cell    (Decrease Signal per step from I Cell)
"""

def createCleanMatrix(layerCount, size):
    for layer in range(layerCount):
        neuralMatrix.append([])
    #print(neuralMatrix)

    for layer in range(len(neuralMatrix)):
        for index in range(size):
            neuralMatrix[layer].append([])
    #print(neuralMatrix)

    for layer in range(len(neuralMatrix)):
        for index in range(size):
            for item in range(size):
                neuralMatrix[layer][item].append("O")
    #print(neuralMatrix, "\n")

def createFirstInput():
    layer = 0
    x = int(ri(1, size-1))
    y = int(ri(1, size-1))
    rowIOLog.append(x)
    columnIOLog.append(y)
    neuralMatrix[layer][x][y] = "I"

def createPaths():
    locateX = int()
    locateY = int()
    for layer in range(len(neuralMatrix)):
        for index in range(size):
            for item in range(size):

                cell = neuralMatrix[layer][index][item]
                if cell == "O":
                    change = str(rc(pathTypeCells))
                    neuralMatrix[layer][index][item] = change
                else:
                    pass

def connectLayerIO():
    index  = 0
    matrixLayers = len(neuralMatrix)
    while index < matrixLayers:
        layer = index
        x = rowIOLog[index]
        y = columnIOLog[index]
        neuralMatrix[layer][x][y] = "I"
        index += 1

def debugPrint():
    #print(neuralMatrix)
    for layer in range(len(neuralMatrix)):
        for row in range(size):
            print(neuralMatrix[layer][row])
        print("\n")

def cleanPrint():
    for layer in range(len(neuralMatrix)):
        tempData = []
        for row in range(size):
            tempData.append(" ".join(neuralMatrix[layer][row]))
        for item in tempData:
            print("{:>1}".format(item))
        print("\n")

layerCount = int(input("Amount of layers: "))
size = int(input("Size: "))

createCleanMatrix(layerCount, size)
debugPrint()
createFirstInput()
print("Before", "\n")
print("###############", "\n")
print("After", "\n")
debugPrint()
print("\n")
cleanPrint()
createPaths()
print("Before", "\n")
print("###############", "\n")
print("After", "\n")
debugPrint()
print("\n")
cleanPrint()




#END
