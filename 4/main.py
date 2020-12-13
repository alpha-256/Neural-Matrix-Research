import math
import uuid
import numpy as np
import pandas as pd
from random import random
from random import uniform
from random import randint as ri
import matplotlib.pyplot as plt

neuralMatrix = []
weightArray = []

def SectionDivider():
    print("\n################################\n")

def generateNeurons(count):
    for n in range(count):
        neuralMatrix.append([])

    for neuronData in neuralMatrix:
        uniformWeight = uniform(0, 1)
        uniformBias = uniform(0, 1)
        neuronData.append(uuid.uuid4().hex)
        neuronData.append([uniformWeight, uniformBias])

def isAllUnique(neuralMatrix):
    seen = set()
    return not any(neuronData[0] in seen or seen.add(neuronData[0]) for neuronData in neuralMatrix)

def neuralMatrixDebug(neuralMatrix):
    SectionDivider()
    print("Neural Matrix Debug Print\n")
    print("Length:\n", len(neuralMatrix), "\n")
    print("Full Print:\n", neuralMatrix, "\n")
    print("Clean Print:")
    for neuron in range(len(neuralMatrix)):
        print(neuralMatrix[neuron])
    print("\n")
    SectionDivider()
    print("Is all unique?", isAllUnique(neuralMatrix))

def simulate():
    for neuron in neuralMatrix:
        for neuronData in neuron:
            print(neuronData[1])

generateNeurons(500)

neuralMatrixDebug(neuralMatrix)

simulate()
