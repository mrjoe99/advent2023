import os

ABSOLUTE_PATH = os.path.dirname(__file__)
DAY = os.path.basename(__file__).split('_')[1].split(".")[0]

class AlmanacMap(object):
    def __init__(self, names, dest_ranges, source_ranges, range_lengths):
        self.names = names
        self._dest_ranges = dest_ranges
        self._source_ranges = source_ranges
        self._range_lengths = range_lengths
        self._custom_maps = {}
        self._populate_maps()

    def _populate_maps(self):
        x = 0
        # name = [name, range, starting index]
        for name in self.names:
            
            for y in range(name[2], name[1]): # index range of map
                destination = self._dest_ranges[y]
                source = self._source_ranges[y]
                range_length = range_lengths[y]

                for z in range(0, range_length):
                    if name[0] not in self._custom_maps.keys():
                        self._custom_maps[name[0]] = {'destinations': [], 'sources': []}

                    self._custom_maps[name[0]]['destinations'].append(destination + z)
                    self._custom_maps[name[0]]['sources'].append(source + z)

                x += 1


def get_input(file):
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

        counter = 0

        for x in range(2, len(input)):
            
            if "map" in input[x]:
                names.append([input[x][:-5], 0, counter]) # name, range, starting index
            elif input[x] != '':
                temp = input[x].split(" ")

                destinations.append(int(temp[0]))
                sources.append(int(temp[1]))
                ranges.append(int(temp[2]))
                names[len(names) - 1][1] += 1
                counter += 1

        return seeds, names, destinations, sources, ranges    


if __name__ == '__main__':
    file = f'{ABSOLUTE_PATH}/advent_data_{DAY}.txt'
    file = f'{ABSOLUTE_PATH}/example_advent_data_{DAY}.txt'

    input = get_input(file)
    seeds, names, dest_ranges, source_ranges, range_lengths = parse_input(input)
    
    maps_collection = AlmanacMap(names, dest_ranges, source_ranges, range_lengths)

    #print(f"ANSWER: {}")

    print(f"\n[COMPLETE] {__file__}")