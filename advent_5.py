import os

ABSOLUTE_PATH = os.path.dirname(__file__)
DAY = os.path.basename(__file__).split('_')[1].split(".")[0]
EXAMPLE = True

class AlmanacMaps(object):

    def __init__(self, name, dest_ranges, source_ranges, range_lengths):
        name = name
        self._dest_ranges = dest_ranges
        self._source_ranges = source_ranges
        self._range_lengths = range_lengths
        self._maps = {}

        self._populate_maps()

    def _populate_maps(self):
        for x in range(0, len(self._dest_ranges)):
            for y in range(0, self._range_lengths):
                print("DEBUG")


def get_input():
    file = f'{ABSOLUTE_PATH}\\advent_data_{DAY}.txt'

    if EXAMPLE:
        file = f'{ABSOLUTE_PATH}\\example_advent_data_{DAY}.txt'

    input = []

    with open(file, 'r') as infile:
        for line in infile:
            input.append(line.strip("\n"))

    return input

def parse_input(input):
    seeds = []
    names = []
    destinations = []
    sources = []
    ranges = []

    seeds = [int(x) for x in input[0][7:].split(" ")]

    for x in range(2, len(input)):
        if "map" in input[x]:
            names.append([input[x][:-5], 0])
        elif input[x] != '':
            temp = input[x].split(" ")

            destinations.append(int(temp[0]))
            sources.append(int(temp[1]))
            ranges.append(int(temp[2]))
            names[len(names) - 1][1] += 1

    print("DEBUG")
    return seeds, names, destinations, sources, ranges




if __name__ == '__main__':
    input = get_input()
    seeds, names, dest_ranges, source_ranges, range_lengths = parse_input(input)

    
    test = AlmanacMap("test", [], [], [])

    test.name
    print("DEBUG")