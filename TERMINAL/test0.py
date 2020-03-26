neuralMatrix = []
layerCount = 2
size = 5

for layer in range(layerCount):
    neuralMatrix.append([])
print(neuralMatrix)

for layer in range(len(neuralMatrix)):
    for index in range(size):
        neuralMatrix[layer].append([])
print(neuralMatrix)

for layer in range(len(neuralMatrix)):
    for index in range(size):
        for item in range(size):
            neuralMatrix[layer][item].append("0")
print(neuralMatrix, "\n")

for layer in range(len(neuralMatrix)):
    for row in range(size):
        print(neuralMatrix[layer][row])
    print("\n")
