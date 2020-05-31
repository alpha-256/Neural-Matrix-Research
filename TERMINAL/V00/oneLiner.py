
from random import randint
from random import choice
from pprint import pprint

"""
I = input   Cell
O = Output  Cell
G = Green   Cell    (Increase signal per step from I Cell)
R = Red     Cell    (Decrease Signal per step from I Cell)
"""

def ayy(layer_count, size):

    layer_matrix = [[choice(["G", "R"]) for _ in range(size)] for _ in range(layer_count)]

    for arr in layer_matrix:
        for _ in range(3):
            randomly_select_idx = randint(0, len(arr)-1)
            arr[randomly_select_idx] = "O"

    randomly_select_idx = randint(0, len(layer_matrix[0])-1)
    layer_matrix[0][randomly_select_idx] = "I"

    return layer_matrix


def lmao(layer_matrix):

    for matrix_idx, curr_layer in enumerate(layer_matrix[1:], start=1):
        for char_idx, char in enumerate(layer_matrix[matrix_idx-1]):
            if char == "O":
                curr_layer[char_idx] = "I"

    return

layer_count = int(input("Layer count > "))
size = int(input("Size > "))

arr = ayy(layer_count, size*size)

print("Generated Layer")
for layer in arr:
    for idx, ele in enumerate(layer):
        if idx % size == 0:
            print()
        print(ele, end=" ")
    print()
print("---")

lmao(arr)

print("Connected Layer")
for layer in arr:
    for idx, ele in enumerate(layer):
        if idx % size == 0:
            print()
        print(ele, end=" ")
    print()
print("---")




#END
