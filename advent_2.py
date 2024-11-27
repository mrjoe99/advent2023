import os

ABSOLUTE_PATH = os.path.dirname(__file__)
DAY = os.path.basename(__file__).split('_')[1].split(".")[0]


def get_input(file):
    input = []

    with open(file, 'r') as infile:
        for line in infile:
            input.append(line.strip('\n')[8:].split(';'))

    for x in range(0, len(input)):

        for y in range(0, len(input[x])):
            input[x][y] = input[x][y].split(',')

            for z in range(0, len(input[x][y])):
                input[x][y][z] = input[x][y][z].strip()

    games = []

    for game in range(0, len(input)):
        matches = []

        for match in range(0, len(input[game])):
            
            for value in range(0, len(input[game][match])):
                draw = {}

                temp = input[game][match][value].split(' ')
                draw[temp[1]] = int(temp[0])

                matches.append(draw)

        games.append(matches)

    return games

def evaluate_games(games):
    results = []

    for game in games:
        standings = {
            'red': 0,
            'green': 0,
            'blue': 0
        }

        for move in game:
            key = list(move)[0]
            value = move[key]

            if value > standings[key]:
                standings[key] = value

        results.append(standings.copy())

        print("DEBUG")
        
    return results

def calculate_powers(games):
    powers = []

    for game in games:
        power = 1
        for color in game:
            power *= game[color]

        powers.append(power)

    return powers

def calculate_sum(powers):
    sum = 0

    for power in powers:
        sum += power
    
    return sum


if __name__ == '__main__':
    file = f'{ABSOLUTE_PATH}/advent_data_{DAY}.txt'
    #file = f'{ABSOLUTE_PATH}/example_advent_data_{DAY}.txt'

    games = get_input(file)
    minimum_cubes_per_game = evaluate_games(games)
    powers = calculate_powers(minimum_cubes_per_game)

    print(calculate_sum(powers))






# import os

# ABSOLUTE_PATH = os.path.dirname(__file__)
# DAY = os.path.basename(__file__).split('_')[1].split(".")[0]


# def get_input(file):
#     input = []

#     with open(file, 'r') as infile:
#         for line in infile:
#             input.append(line.strip('\n')[8:].split(';'))

#     for x in range(0, len(input)):

#         for y in range(0, len(input[x])):
#             input[x][y] = input[x][y].split(',')

#             for z in range(0, len(input[x][y])):
#                 input[x][y][z] = input[x][y][z].strip()

#     games = []

#     for game in range(0, len(input)):
#         matches = []

#         for match in range(0, len(input[game])):
            
#             for value in range(0, len(input[game][match])):
#                 draw = {}

#                 temp = input[game][match][value].split(' ')
#                 draw[temp[1]] = int(temp[0])

#                 matches.append(draw)

#         games.append(matches)

#     return games

# def evaluate_games(bag_contents, games):
#     possible_ids = []

#     for game_index in range(0, len(games)):
#         possible = True

#         if possible:
#             for match in range(0, len(games[game_index])):
#                 result = evaluate_match(bag_contents, games[game_index][match])

#                 if not result:
#                     possible = False
        
#         if possible:
#             possible_ids.append(game_index + 1)

#     return possible_ids

# def evaluate_match(contents, match):
#     for key in match.keys():
#         if contents[key] < match[key]:
#             return False
    
#     return True


# if __name__ == '__main__':
#     # file = f'{ABSOLUTE_PATH}/advent_data_{DAY}.txt'
#     file = f'{ABSOLUTE_PATH}/example_advent_data_{DAY}.txt'

#     bag_contents = {
#         "red": 12,
#         "green": 13,
#         "blue": 14
#     }
    
#     games = get_input(file)
#     possible_games = evaluate_games(bag_contents, games)

#     print(f"ID Total: {sum(possible_games)}")

#     print("DEBUG")