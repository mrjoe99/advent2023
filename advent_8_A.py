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
    current_position = "AAA"
    pattern_position = 0

    while current_position != "ZZZ":
        if pattern_position >= (len(pattern) - 1):
            pattern_position -= len(pattern)
        
        direction = pattern[pattern_position]
        if direction == "L":
            direction = 0
        else:
            direction = 1

        current_position = network[current_position][direction]
        
        steps += 1
        pattern_position += 1


    return steps
    print("DEBUG")


if __name__ == "__main__":
    file = f"{ABSOLUTE_PATH}/advent_data_{DAY}.txt"
    #file = f"{ABSOLUTE_PATH}/example_advent_data_{DAY}.txt"

    pattern, network = get_input(file)
    steps = navigate_desert(pattern, network)

    print(f"ANSWER: {steps}")
    print(f"\n[COMPLETE] {__file__}")