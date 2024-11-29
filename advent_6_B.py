import os

ABSOLUTE_PATH = os.path.dirname(__file__)
DAY = os.path.basename(__file__).split('_')[1].split(".")[0]

def get_input(file):
    input = []

    with open(file, 'r') as infile:
        for line in infile:
            input.append(int(line.strip("\n").split(":")[1].replace(" ", "")))
            
    return input[0], input[1]

def calculate_options(time):
    options = []
    button_pressed = 0

    while button_pressed <= time:
        distance = (time - button_pressed) * button_pressed
        options.append([button_pressed, distance])

        button_pressed += 1

    return options

def calculate_winners(options, record):
    # option item entry format: [button_pressed, distance]
    winners = []

    for option in options:
            if option[1] > record:
                winners.append(option)

    return winners


if __name__ == '__main__':
    file = f'{ABSOLUTE_PATH}/advent_data_{DAY}.txt'
    #file = f'{ABSOLUTE_PATH}/example_advent_data_{DAY}.txt'

    time, record = get_input(file)
    options = calculate_options(time)
    winning_options = calculate_winners(options, record)
    
    print(f"ANSWER: {len(winning_options)}")

    print(f"\n[COMPLETE] {__file__}")