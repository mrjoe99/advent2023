import os

ABSOLUTE_PATH = os.path.dirname(__file__)
DAY = os.path.basename(__file__).split('_')[1].split(".")[0]

def get_input(file):
    input = []

    with open(file, 'r') as infile:
        for line in infile:
            input.append(line.strip("\n").split(":")[1].split(" "))

    times = []
    records = []

    for x in range(len(input)):
        if x == 0:
            for value in input[x]:
                if value != '':
                    times.append(int(value))
        else:
            for value in input[x]:
                if value != '':
                    records.append(int(value))
            
    return times, records

def calculate_options(times):
    options = {}
    
    for time in times:
        button_pressed = 0
        options[str(time)] = []

        while button_pressed <= time:
            distance = (time - button_pressed) * button_pressed
            options[str(time)].append([button_pressed, distance])

            button_pressed += 1

    return options

def calculate_winners(options, records):
    # option item entry format: [button_pressed, distance]
    winners = {}

    for x, key in enumerate(options):
        winners[key] = []

        for item in options[key]:
            if item[1] > records[x]:
                winners[key].append(item)

    return winners

def calculate_margin_of_error(options):
    margin = 1

    for key in options:
        margin *= len(options[key])

    return margin


if __name__ == '__main__':
    file = f'{ABSOLUTE_PATH}/advent_data_{DAY}.txt'
    #file = f'{ABSOLUTE_PATH}/example_advent_data_{DAY}.txt'

    times, records = get_input(file)
    options = calculate_options(times)
    winning_options = calculate_winners(options, records)
    
    print(f"ANSWER: {calculate_margin_of_error(winning_options)}")

    print(f"\n[COMPLETE] {__file__}")