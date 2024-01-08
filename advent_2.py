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

def evaluate_games(bag_contents, games):
    possible_ids = []

    for game_index in range(0, len(games)):
        possible = True

        if possible:
            contents = bag_contents.copy()
            for match in range(0, len(games[game_index])):
                result, contents = evaluate_match(contents, games[game_index][match])

                if not result:
                    possible = False
        
        if possible:
            possible_ids.append(game_index + 1)

    return possible_ids

def evaluate_match(contents, match):
    for key, value in match.items():
        contents[key] -= match[key]

    for value in contents.values():
        if value < 0:
            return False, contents
        
    return True, contents


if __name__ == '__main__':
    bag_contents = {
        "red": 12,
        "green": 13,
        "blue": 14
    }
    
    games = get_input()
    possible_games = evaluate_games(bag_contents, games)

    print(f"ID Total: {sum(possible_games)}")

    print("DEBUG")