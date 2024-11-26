import os

ABSOLUTE_PATH = os.path.dirname(__file__)
DAY = os.path.basename(__file__).split('_')[1].split(".")[0]
EXAMPLE = False

def get_input():
    file = f'{ABSOLUTE_PATH}/advent_data_{DAY}.txt'

    if EXAMPLE:
        file = f'{ABSOLUTE_PATH}/example_advent_data_{DAY}.txt'

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
        
        wins.append(len(temp))

    return wins

def determine_scores(results):
    scores = []

    for result in results:
        if result > 0:
            scores.append(2 ** (result - 1))
        else:
            scores.append(0)

    return scores

def simulate_game(card_counts, card_wins, start):
    for y in range(0, card_wins[x]):
        card_counts[x + 1 + y] += 1 * card_counts[x]

    return card_counts


if __name__ == '__main__':
    input = get_input()
    cards = parse_input(input)
    winning_card_numbers = calculate_wins(cards)

    card_counts = [1 for x in range(0, len(winning_card_numbers))]

    for x in range(0, len(winning_card_numbers)):
        card_counts = simulate_game(card_counts, winning_card_numbers, x)

    sum = 0

    for count in card_counts:
        sum += count

    print(sum)

#### PART 1 ####
    
#     def get_input():
#     file = f'{ABSOLUTE_PATH}\\advent_data_{DAY}.txt'

#     if EXAMPLE:
#         file = f'{ABSOLUTE_PATH}\\example_advent_data_{DAY}.txt'

#     input = []

#     with open(file, 'r') as infile:
#         for line in infile:
#             input.append(line.strip("\n"))

#     return input

# def parse_input(input):
#     cards = []

#     for line in input:
#         temp = line.split("|")
#         temp[0] = temp[0].split(":")[1].strip().split(" ")
#         temp[0] = [int(x) for x in temp[0] if x != '']

#         temp[1] = temp[1].strip().split(" ")
#         temp[1] = [int(x) for x in temp[1] if x != '']

#         cards.append(temp)

#     return cards

# def calculate_wins(cards):
#     wins = []

#     for card in cards:
#         temp = []

#         winning_numbers = card[0]
#         my_numbers = card[1]

#         for number in my_numbers:
#             if number in winning_numbers:
#                 temp.append(number)
        
#         wins.append(temp)

#     return wins

# def determine_score(numbers):
#     score = 0

#     for result in numbers:
#         if len(result) > 0:
#             score += 2 ** (len(result) - 1)

#     print(score)


# if __name__ == '__main__':
#     input = get_input()
#     cards = parse_input(input)
#     winning_numbers = calculate_wins(cards)
#     determine_score(winning_numbers)