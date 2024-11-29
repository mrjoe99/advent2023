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

def remove_non_symbol_adjacent(numbers, symbols):
    confirmed_numbers = []

    for number in numbers:
        valid = check_numbers(number, symbols)

        if valid:
            confirmed_numbers.append(number)

    return confirmed_numbers

def check_numbers(number, symbols):
    # Note: symbol is anchor point
    #    => check above left = symbol is above and left of number
    functions = {
        check_above_left(number, symbols),
        check_above(number, symbols),
        check_above_right(number, symbols),
        check_left(number, symbols),
        check_right(number, symbols),
        check_below_left(number, symbols),
        check_below(number, symbols),
        check_below_right(number, symbols)
    }

    for valid_result in functions:
        if valid_result:
            return True
        
    # valid1 = check_above_left(number, symbols)
    # valid2 = check_above(number, symbols)
    # valid3 = check_above_right(number, symbols)
    # valid4 = check_left(number, symbols)
    # valid5 = check_right(number, symbols)
    # valid6 = check_below_left(number, symbols)
    # valid7 = check_below(number, symbols)
    # valid8 = check_below_right(number, symbols)

    # return valid1 or valid2 or valid3 or valid4 or valid5 or valid6 or valid7 or valid8

def check_above_left(number, symbols):
    for position in number[1]:
        y = position[0] - 1
        x = position[1] - 1

        for symbol in symbols:
            if [y, x] == symbol[1]:
                return True
    
    return False
            
def check_above(number, symbols):
    for position in number[1]:
        y = position[0] - 1
        x = position[1]

        for symbol in symbols:
            if [y, x] == symbol[1]:
                return True
            
    return False

def check_above_right(number, symbols):
    for position in number[1]:
        y = position[0] - 1
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
        y = position[0] + 1
        x = position[1] - 1

        for symbol in symbols:
            if [y, x] == symbol[1]:
                return True
            
    return False
            
def check_below(number, symbols):
    for position in number[1]:
        y = position[0] + 1
        x = position[1]

        for symbol in symbols:
            if [y, x] == symbol[1]:
                return True
            
    return False

def check_below_right(number, symbols):
    for position in number[1]:
        y = position[0] + 1
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
    file = f'{ABSOLUTE_PATH}/advent_data_{DAY}.txt'
    file = f'{ABSOLUTE_PATH}/example_advent_data_{DAY}.txt'

    non_symbols = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "."]
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    input = get_input(file)
    symbols, symbol_characters, numbers = find_symbols_and_numbers(input, non_symbols, digits)
    numbers = convert_numbers(numbers, digits)
    numbers = remove_non_symbol_adjacent(numbers, symbols)

    calculate_sum(numbers)








# # Part 1
 
# import os

# ABSOLUTE_PATH = os.path.dirname(__file__)
# DAY = os.path.basename(__file__).split('_')[1].split(".")[0]

# def get_input(file):
#     input = []

#     with open(file, 'r') as infile:
#         for line in infile:
#             input.append(line.strip("\n"))

#     return input

# def find_symbols_and_numbers(input, non_symbols, digits):
#     symbols = []
#     numbers = []
    
#     for y, line in enumerate(input):
#         for x, item in enumerate(line):
#             if item not in non_symbols:
#                 symbols.append([item, [y, x]])
#                 numbers.append([item, [y, x]])
#             else:
#                 numbers.append([item, [y, x]])

#     characters = set()

#     for symbol in symbols:
#         characters.add(symbol[0])

#     return symbols, list(characters), numbers

# def convert_numbers(numbers, digits):
    
#     number_series = []
#     converted_numbers = []

#     for number in numbers:
#         if number[0] in digits:
#             number_series.append(number)
#         else:
#             if number[0] not in digits:
#                 converted_numbers.append(convert_to_decimal(number_series))
#                 number_series = []

#     for x in range(len(converted_numbers) - 1, 0, -1):
#         if converted_numbers[x] == [0, []]:
#             converted_numbers.pop(x)

#     return converted_numbers

# def convert_to_decimal(number_series):
#     power = len(number_series) - 1
#     sum = 0

#     for x in range(0, len(number_series)):
#         sum += 10 ** power * int(number_series[x][0])
#         power -= 1

#     locations = []

#     for value in number_series:
#         locations.append(value[1])

#     return [sum, locations]

# def remove_non_symbol_adjacent(numbers, symbols):
#     confirmed_numbers = []

#     for number in numbers:
#         valid = check_numbers(number, symbols)

#         if valid:
#             confirmed_numbers.append(number)

#     return confirmed_numbers

# def check_numbers(number, symbols):
#     # Note: symbol is anchor point
#     #    => check above left = symbol is above and left of number
#     functions = {
#         check_above_left(number, symbols),
#         check_above(number, symbols),
#         check_above_right(number, symbols),
#         check_left(number, symbols),
#         check_right(number, symbols),
#         check_below_left(number, symbols),
#         check_below(number, symbols),
#         check_below_right(number, symbols)
#     }

#     for valid_result in functions:
#         if valid_result:
#             return True

# def check_above_left(number, symbols):
#     for position in number[1]:
#         y = position[0] - 1
#         x = position[1] - 1

#         for symbol in symbols:
#             if [y, x] == symbol[1]:
#                 return True
    
#     return False
            
# def check_above(number, symbols):
#     for position in number[1]:
#         y = position[0] - 1
#         x = position[1]

#         for symbol in symbols:
#             if [y, x] == symbol[1]:
#                 return True
            
#     return False

# def check_above_right(number, symbols):
#     for position in number[1]:
#         y = position[0] - 1
#         x = position[1] + 1

#         for symbol in symbols:
#             if [y, x] == symbol[1]:
#                 return True
            
#     return False
            
# def check_left(number, symbols):
#     for position in number[1]:
#         y = position[0]
#         x = position[1] - 1

#         for symbol in symbols:
#             if [y, x] == symbol[1]:
#                 return True
            
#     return False

# def check_right(number, symbols):
#     for position in number[1]:
#         y = position[0]
#         x = position[1] + 1

#         for symbol in symbols:
#             if [y, x] == symbol[1]:
#                 return True
            
#     return False

# def check_below_left(number, symbols):
#     for position in number[1]:
#         y = position[0] + 1
#         x = position[1] - 1

#         for symbol in symbols:
#             if [y, x] == symbol[1]:
#                 return True
            
#     return False
            
# def check_below(number, symbols):
#     for position in number[1]:
#         y = position[0] + 1
#         x = position[1]

#         for symbol in symbols:
#             if [y, x] == symbol[1]:
#                 return True
            
#     return False

# def check_below_right(number, symbols):
#     for position in number[1]:
#         y = position[0] + 1
#         x = position[1] + 1

#         for symbol in symbols:
#             if [y, x] == symbol[1]:
#                 return True

#     return False

# def calculate_sum(numbers):
#     sum = 0

#     for number in numbers:
#         sum += number[0]

#     print(sum)


# if __name__ == '__main__':
#     file = f'{ABSOLUTE_PATH}/advent_data_{DAY}.txt'
#     file = f'{ABSOLUTE_PATH}/example_advent_data_{DAY}.txt'

#     non_symbols = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "."]
#     digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

#     input = get_input(file)
#     symbols, symbol_characters, numbers = find_symbols_and_numbers(input, non_symbols, digits)
#     numbers = convert_numbers(numbers, digits)
#     numbers = remove_non_symbol_adjacent(numbers, symbols)

#     calculate_sum(numbers)