import os

ABSOLUTE_PATH = os.path.dirname(__file__)
DAY = os.path.basename(__file__).split('_')[1].split(".")[0]

def get_input(file):
    input = []

    with open(file, 'r') as infile:
        for line in infile:
            input.append(line.strip("\n"))

    return input

def find_symbols_and_numbers(input, non_symbols, digits):
    symbols = []
    numbers = []
    
    for y, line in enumerate(input):
        for x, item in enumerate(line):
            if item not in non_symbols:
                symbols.append([item, [y, x]])
                numbers.append([item, [y, x]])
            else:
                numbers.append([item, [y, x]])

    characters = set()

    for symbol in symbols:
        characters.add(symbol[0])

    return symbols, list(characters), numbers

def convert_numbers(numbers, digits):
    number_series = []
    converted_numbers = []

    for number in numbers:
        if number[0] in digits:
            number_series.append(number)
        else:
            if number[0] not in digits:
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

def remove_non_gears(numbers, symbols):
    confirmed_gears = []

    for symbol in symbols:
        result = check_symbols(numbers, symbol)

        if isinstance(result, list):
            confirmed_gears.append(result)

    return confirmed_gears

def check_symbols(numbers, symbol):
    # check if NUMBER is above left, below, etc relative to SYMBOL

    functions = [
        check_above_left(numbers, symbol),
        check_above(numbers, symbol),
        check_above_right(numbers, symbol),
        check_left(numbers, symbol),
        check_right(numbers, symbol),
        check_below_left(numbers, symbol),
        check_below(numbers, symbol),
        check_below_right(numbers, symbol)
    ]

    adjacent = set()

    for result in functions:
        if result != False:
            adjacent.add(result[0])

    if len(adjacent) == 2:
        return list(adjacent)
    
    return False

def check_above_left(numbers, symbol):
    for number in numbers:
        for position in number[1]:
            y = position[0] + 1
            x = position[1] + 1

            if [y, x] == symbol[1]:
                return number
        
    return False
            
def check_above(numbers, symbol):
    for number in numbers:
        for position in number[1]:
            y = position[0] + 1
            x = position[1]

            if [y, x] == symbol[1]:
                return number
        
    return False

def check_above_right(numbers, symbol):
    for number in numbers:
        for position in number[1]:
            y = position[0] + 1
            x = position[1] - 1

            if [y, x] == symbol[1]:
                return number
        
    return False
            
def check_left(numbers, symbol):
    for number in numbers:
        for position in number[1]:
            y = position[0]
            x = position[1] + 1

            if [y, x] == symbol[1]:
                return number
        
    return False

def check_right(numbers, symbol):
    for number in numbers:
        for position in number[1]:
            y = position[0]
            x = position[1] - 1

            if [y, x] == symbol[1]:
                return number
        
    return False

def check_below_left(numbers, symbol):
    for number in numbers:
        for position in number[1]:
            y = position[0] - 1
            x = position[1] + 1

            if [y, x] == symbol[1]:
                return number
        
    return False
            
def check_below(numbers, symbol):
    for number in numbers:
        for position in number[1]:
            y = position[0] - 1
            x = position[1]

            if [y, x] == symbol[1]:
                return number
                
    return False

def check_below_right(numbers, symbol):
    for number in numbers:
        for position in number[1]:
            y = position[0] - 1
            x = position[1] - 1

            if [y, x] == symbol[1]:
                return number
        
    return False

def remove_non_asterisk_symbols(symbols):
    asterisks = []

    for symbol in symbols:
        if symbol[0] == "*":
            asterisks.append(symbol)

    return asterisks

def calculate_gear_ratios(gears):
    ratios = []

    for gear in gears:
        ratios.append(gear[0] * gear[1])

    return ratios

def calculate_sum(ratios):
    sum = 0

    for ratio in ratios:
        sum += ratio
    
    return sum


if __name__ == '__main__':
    file = f'{ABSOLUTE_PATH}/advent_data_{DAY}.txt'
    #file = f'{ABSOLUTE_PATH}/example_advent_data_{DAY}.txt'

    non_symbols = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "."]
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    input = get_input(file)
    symbols, symbol_characters, numbers = find_symbols_and_numbers(input, non_symbols, digits)
    numbers = convert_numbers(numbers, digits)
    symbols = remove_non_asterisk_symbols(symbols)
    gears = remove_non_gears(numbers, symbols)
    ratios = calculate_gear_ratios(gears)

    print(f"ANSWER: {calculate_sum(ratios)}")

    print(f"\n[COMPLETE] {__file__}")