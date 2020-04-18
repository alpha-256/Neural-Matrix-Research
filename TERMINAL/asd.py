
from random import randint
from random import choice


def prep(layer_count, elements_count):

    # Generate layers
    layer_matrix = []
    for layer in range(layer_count):
        
        arr = []
        for _ in range(elements_count):
            char = choice(["G", "R"])
            arr.append(char)
        
        layer_matrix.append(arr)

    return layer_matrix

def ayy(layer_matrix, oh_per_layer=3):
    
    # For each layer, randomly select 3 position for "O"
    # Note: The position can overlap
    for arr in layer_matrix:
        for _ in range(oh_per_layer):
            randomly_select_idx = randint(0, len(arr)-1)
            arr[randomly_select_idx] = "O"
    
    return

def lmao(layer_matrix):

    # Randomly insert "I" in the 1st layer (index 0 layer)
    randomly_select_idx = randint(0, len(layer_matrix[0])-1)
    layer_matrix[0][randomly_select_idx] = "I"

    return

def blaze_it(layer_matrix):

    # Start from the 2nd layer (Index of 1)
    # loop through elements of the previous layer (matrix_idx - 1)
    for matrix_idx, current_layer in enumerate(layer_matrix[1:], start=1):
        previous_layer = layer_matrix[matrix_idx-1]
        for char_idx, char in enumerate(previous_layer):
            
            # If "O" is found, replace the current layer of the same
            # index with "I"
            if char == "O":
                current_layer[char_idx] = "I"
    
    return

def print_all_layers(layer_matrix, size):
    # For printing the layers
    for layer in layer_matrix:

        for idx, ele in enumerate(layer):
            if idx % size == 0:
                print()
            print(ele, end=" ")
        print()

    return


def _main():

    layer_count = int(input("Layer count > "))
    size = int(input("Size > "))

    bong = prep(layer_count, size*size)
    ayy(bong, 3)
    lmao(bong)

    print("Generated Layer")
    print_all_layers(bong, size)
    print("---")

    blaze_it(bong)

    print("Connected Layer")
    print_all_layers(bong, size)
    print("---")


if __name__ == "__main__":
    _main()

