import os

ABSOLUTE_PATH = os.path.dirname(__file__)
DAY = os.path.basename(__file__).split('_')[1].split(".")[0]
EXAMPLE = False

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
    cards = []

    for line in input:
        temp = line.split("|")
        temp[0] = temp[0].split(":")[1].strip().split(" ")
        temp[0] = [int(x) for x in temp[0] if x != '']

        temp[1] = temp[1].strip().split(" ")
        temp[1] = [int(x) for x in temp[1] if x != '']

        cards.append(temp)

    return cards

def calculate_wins(cards):
    wins = []

    for card in cards:
        temp = []

        winning_numbers = card[0]
        my_numbers = card[1]

        for number in my_numbers:
            if number in winning_numbers:
                temp.append(number)
        
        wins.append(temp)

    return wins

def determine_score(numbers):
    score = 0

    for result in numbers:
        if len(result) > 0:
            score += 2 ** (len(result) - 1)

    print(score)


if __name__ == '__main__':
    input = get_input()
    cards = parse_input(input)
    winning_numbers = calculate_wins(cards)
    determine_score(winning_numbers)