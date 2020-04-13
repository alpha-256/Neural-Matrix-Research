from random import randint as ri
from random import choice as rc

pathMatrix = []
IOLog = []
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
        pathMatrix.append([])
    #print(pathMatrix)

    for layer in range(len(pathMatrix)):
        for index in range(size):
            pathMatrix[layer].append([])
    #print(pathMatrix)

    for layer in range(len(pathMatrix)):
        for index in range(size):
            for item in range(size):
                pathMatrix[layer][item].append("O")
    #print(pathMatrix, "\n")

def createFirstInput():
    layer = 0
    index = int(ri(1, size-1))
    item = int(ri(1, size-1))
    pathMatrix[layer][index][item] = "I"

def createPaths():
    for layer in range(len(pathMatrix)):
        for index in range(size):
            for item in range(size):
                cell = pathMatrix[layer][index][item]
                if cell == "O":
                    change = str(rc(pathTypeCells))
                    pathMatrix[layer][index][item] = change
                else:
                    pass

def create3OutputCells():
    tempLog = []
    for layer in range(len(pathMatrix)):
        tempLog.append([])
    for iteration in range(3):
        for layer in range(len(pathMatrix)):
            index = ri(0, size - 1)
            item = ri(0, size - 1)
            pathMatrix[layer][index][item] = "O"
            tempLog[layer].append([index, item])
    for layer in range(len(tempLog)):
        IOLog.append(tempLog[layer])

def connectIO():
    holdY = int()
    holdX = int()
    for layer in range(len(IOLog)):
        for index in range(len(IOLog[layer])):
            for coordinates in range(len(IOLog[layer][index])):
                print(IOLog[layer][index][coordinates])
                if coordinates == 0:
                    holdY = int(IOLog[layer][index][coordinates])
                elif coordinates == 1:
                    holdX = int(IOLog[layer][index][coordinates])
                else:
                    raise Exception("OUT OF RANGE!")

                if coordinates == 0:
                    holdY = int(IOLog[layer][index][coordinates])
                elif coordinates == 1:
                    holdX = int(IOLog[layer][index][coordinates])
                else:
                    raise Exception("OUT OF RANGE!")
                for matrixLayers in range(len(pathMatrix)):
                    if matrixLayers < layerCount:
                        matrixLayers += 1
                        print(matrixLayers)
                        pathMatrix[matrixLayers][holdY][holdX] = "I"
                        matrixLayers -= 1
                    elif matrixLayers >= layerCount:
                        pass
                    else:
                        pass

    #tempYIndex = yLog[len(yLog)]
    #tempXIndex = xLog[len(xLog)]

def debugPrint():
    #print(pathMatrix)
    for layer in range(len(pathMatrix)):
        for row in range(size):
            print(pathMatrix[layer][row])
        print("\n")

def cleanPrint():
    for layer in range(len(pathMatrix)):
        tempData = []
        for row in range(size):
            tempData.append(" ".join(pathMatrix[layer][row]))
        for item in tempData:
            print("{:>1}".format(item))
        print("\n")

layerCount = int(input("Amount of layers: "))
size = int(input("Size: "))

createCleanMatrix(layerCount, size)
createFirstInput()

cleanPrint()

createPaths()
create3OutputCells()

cleanPrint()
print(IOLog)

connectIO()

#cleanPrint()
#print(" Before \n ###### \n After \n")
#cleanPrint()

debugPrint()




#END
