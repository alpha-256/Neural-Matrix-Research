from random import randint
from random import random

def createNetwork(neuronCount):
    for neurons in range(neuronCount):
        tempArray = []
        for n in range(neuronCount):
            if n == neurons :
                pass
            else:
                weights = random()
                neuron = [n, weights]
                tempArray.append(neuron)
        neuralArray.append(tempArray)

    return neuralArray

def cleanPrint(neuralArray):
    for neurons in range(len(neuralArray)):
        print("Neuron", neurons)
        for data in range(len(neuralArray[neurons])):
            print(neuralArray[neurons][data])
            print("")

global neuralArray
global hiddenLayers
global hiddenLayerSize

hiddenLayerSize = int()
hiddenLayers = int()
neuralArray = list()

createNetwork(5)
cleanPrint(neuralArray)
print(neuralArray)
