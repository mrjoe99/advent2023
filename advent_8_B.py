import os

ABSOLUTE_PATH = os.path.dirname(__file__)
DAY = os.path.basename(__file__).split("_")[1].split(".")[0]

def get_input(file):
    input = []

    with open(file, "r") as infile:
        for line in infile:
            input.append(line.strip("\n"))

    pattern = ""
    network = {}

    for line in input:
        if len(line) > 0:
            if "=" not in line:
                pattern = line
            else:
                network[line[0:3]] = [line[7:10], line[12:15]]

    return pattern, network

def navigate_desert(pattern, network):
    steps = 0
    pattern_position = 0
    current_positions = find_starting_positions(network)

    while not final_positions(current_positions):
        for x, current_position in enumerate(current_positions):
            if pattern_position >= (len(pattern) - 1):
                pattern_position -= len(pattern) - 1
            
            direction = pattern[pattern_position]

            if direction == "L":
                direction = 0
            else:
                direction = 1

            current_positions[x] = network[current_position][direction]
            
        steps += 1
        pattern_position += 1

    return steps

def find_starting_positions(network):
    positions = []

    for item in network.keys():
        if item[-1] == "A":
            positions.append(item)
    
    return positions

def final_positions(positions):
    for position in positions:
        if position[len(position) - 1] != "Z":
            return False
        
    return True


if __name__ == "__main__":
    file = f"{ABSOLUTE_PATH}/advent_data_{DAY}.txt"
    #file = f"{ABSOLUTE_PATH}/example_advent_data_{DAY}.txt"

    pattern, network = get_input(file)
    steps = navigate_desert(pattern, network)

    print(f"ANSWER: {steps}")
    print(f"\n[COMPLETE] {__file__}")