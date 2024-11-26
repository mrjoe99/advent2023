import os

ABSOLUTE_PATH = os.path.dirname(__file__)
DAY = os.path.basename(__file__).split('_')[1].split(".")[0]
EXAMPLE = True

def get_input():
    file = f'{ABSOLUTE_PATH}/advent_data_{DAY}.txt'

    if EXAMPLE:
        file = f'{ABSOLUTE_PATH}/example_advent_data_{DAY}.txt'

    input = []

    with open(file, 'r') as infile:
        for line in infile:
            input.append([int(x) for x in line.strip("\n").split(" ")])

    return input

def get_differences(history):
    difference_sequences = []

    for sequence in history:
        temp = []
        temp.append(calculate_differences(sequence))

def calculate_differences(sequence):
    iterations = [sequence.copy()]
    temp = []

    for x in range(0, len(iterations) - 1):
            temp.append(iterations[x + 1] - iterations[x])

    iterations.append(temp)

    while sum(iterations[len(iterations) - 1]) > 0:
        temp = []

        for x in range(0, len(iterations) - 1):
            temp.append(iterations[x + 1] - iterations[x])
        
        iterations.append(temp)
    

        print("DEBUG")

if __name__ == '__main__':
    history = get_input()
    sequenced_differences = get_differences(history)

    print("DEBUG")