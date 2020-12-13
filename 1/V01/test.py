from random import randint
from random import random

global neuralArray
global hiddenLayerSize

hiddenLayerSize = 5
hiddenLayers = 2
neuralArray = list()

def createNetwork(hiddenLayerSize):
    global hiddenLayers
    inputLayer = 1
    outputLayer = 1
    hiddenLayers += inputLayer
    hiddenLayers += outputLayer
    for layer in range(hiddenLayers):
        tempArray = []
        for neurons in range(hiddenLayerSize):
            neuron = []
            for n in range(hiddenLayerSize):
                weights = random()
                neuronData = [n, weights]
                neuron.append(neuronData)
            tempArray.append(neuron)
        neuralArray.append(tempArray)

    return neuralArray

def cleanPrint(neuralArray):
    for layer in range(len(neuralArray)):
        print("Layer #:", layer, "\n")
        for neurons in range(len(neuralArray[layer])):
            for item in range(len(neuralArray[layer][neurons])):
                print(neuralArray[layer][neurons][item])
            print("")

createNetwork(hiddenLayerSize)
cleanPrint(neuralArray)
#print(neuralArray)
