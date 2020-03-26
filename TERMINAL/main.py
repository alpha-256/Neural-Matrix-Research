from random import randint as ri
from pprint import pprint

neuralMatrix = []

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

def mutateAddInput():
    for layer in range(len(neuralMatrix)):
        neuralMatrix[layer][ri(1, size-1)][ri(1, size-1)] = "I"

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
mutateAddInput()
print("Before", "\n")
print("###############", "\n")
print("After", "\n")
debugPrint()
print("\n")
cleanPrint()
