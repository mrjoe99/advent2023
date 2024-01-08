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

def find_symbols_and_numbers(input, non_symbols):
    symbols = []
    numbers = []
    
    for y, line in enumerate(input):
        for x, item in enumerate(line):
            if item not in non_symbols:
                symbols.append([item, [y, x]])
            else:
                numbers.append([item, [y, x]])

    characters = set()

    for symbol in symbols:
        characters.add(symbol[0])

    return symbols, list(characters), numbers

def convert_numbers(numbers, non_symbols):
    number_series = []
    converted_numbers = []

    for number in numbers:
        if number[0] in non_symbols and number[0] != ".":
            number_series.append(number)
        else:
            if number[0] in non_symbols and number[0] == ".":
                converted_numbers.append(convert_to_decimal(number_series))
                number_series = []

    for x in range(len(converted_numbers) - 1, 0, -1):
        if converted_numbers[x] == [0, []]:
            converted_numbers.pop(x)

    return converted_numbers

def convert_to_decimal(number_series):
    power = len(number_series) - 1
    sum = 0

    for x in range(0, len(number_series)):
        sum += 10 ** power * int(number_series[x][0])
        power -= 1

    locations = []

    for value in number_series:
        locations.append(value[1])

    return [sum, locations]

def remove_non_symbol_adjacent(numbers, symbols):
    confirmed_numbers = []
    confirmed = False

    for number in numbers:
        if not confirmed:
            valid = check_numbers(number, symbols)

            if valid:
                confirmed_numbers.append(number)

    return confirmed_numbers

def check_numbers(number, symbols):
    valid1 = check_above_left(number, symbols)
    valid2 = check_above(number, symbols)
    valid3 = check_above_right(number, symbols)
    valid4 = check_left(number, symbols)
    valid5 = check_right(number, symbols)
    valid6 = check_below_left(number, symbols)
    valid7 = check_below(number, symbols)
    valid8 = check_below_right(number, symbols)

    return valid1 or valid2 or valid3 or valid4 or valid5 or valid6 or valid7 or valid8

def check_above_left(number, symbols):
    for position in number[1]:
        y = position[0] + 1
        x = position[1] - 1

        for symbol in symbols:
            if [y, x] == symbol[1]:
                return True
    
    return False
            
def check_above(number, symbols):
    for position in number[1]:
        y = position[0] + 1
        x = position[1]

        for symbol in symbols:
            if [y, x] == symbol[1]:
                return True
            
    return False

def check_above_right(number, symbols):
    for position in number[1]:
        y = position[0] + 1
        x = position[1] + 1

        for symbol in symbols:
            if [y, x] == symbol[1]:
                return True
            
    return False
            
def check_left(number, symbols):
    for position in number[1]:
        y = position[0]
        x = position[1] - 1

        for symbol in symbols:
            if [y, x] == symbol[1]:
                return True
            
    return False

def check_right(number, symbols):
    for position in number[1]:
        y = position[0]
        x = position[1] + 1

        for symbol in symbols:
            if [y, x] == symbol[1]:
                return True
            
    return False

def check_below_left(number, symbols):
    for position in number[1]:
        y = position[0] - 1
        x = position[1] - 1

        for symbol in symbols:
            if [y, x] == symbol[1]:
                return True
            
    return False
            
def check_below(number, symbols):
    for position in number[1]:
        y = position[0] - 1
        x = position[1]

        for symbol in symbols:
            if [y, x] == symbol[1]:
                return True
            
    return False

def check_below_right(number, symbols):
    for position in number[1]:
        y = position[0] - 1
        x = position[1] + 1

        for symbol in symbols:
            if [y, x] == symbol[1]:
                return True

    return False

def calculate_sum(numbers):
    sum = 0

    for number in numbers:
        sum += number[0]

    print(sum)


if __name__ == '__main__':
    non_symbols = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "."]

    input = get_input()
    symbols, symbol_characters, numbers = find_symbols_and_numbers(input, non_symbols)
    numbers = convert_numbers(numbers, non_symbols)
    numbers = remove_non_symbol_adjacent(numbers, symbols)

    calculate_sum(numbers)

    # 6341604: too high
    # 6000000: too high