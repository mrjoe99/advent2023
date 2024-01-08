import os

ABSOLUTE_PATH = os.path.dirname(__file__)
DAY = os.path.basename(__file__).split('_')[1].split(".")[0]
EXAMPLE = True

def get_input():
    file = f'{ABSOLUTE_PATH}\\advent_data_{DAY}.txt'

    if EXAMPLE:
        file = f'{ABSOLUTE_PATH}\\example_advent_data_{DAY}.txt'

    input = []

    with open(file, 'r') as infile:
        for line in infile:
            input.append(line.strip("\n"))

    return input


if __name__ == '__main__':
    input = get_input()

    print("DEBUG")