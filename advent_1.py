import os
import re
from functools import reduce

ABSOLUTE_PATH = os.path.dirname(__file__)
DAY = 1

digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
words = ["zero", "one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
word_conversions = {
        "zero": '0',
        "one": '1',
        "two": '2',
        "three": '3',
        "four": '4',
        "five": '5',
        "six": '6',
        "seven": '7',
        "eight": '8',
        "nine": '9'
    }


def get_input(file):
    with open(file, 'r') as input:
        temp = []

        for line in input:
            temp.append(line.strip('\n'))

        return temp
    
def extract_numerical_calibration_values(input):
    values = []

    for line in input:
        line_values = {}

        for x in range(0, len(line)):
            if line[x] in digits:
                if line[x] not in line_values.keys():
                    line_values[line[x]] = []

                line_values[line[x]].append(x)

        values.append(line_values)

    return values

def find_text(line):
    matches = {}
    
    for word in words:
        # using re.finditer() to find all occurrences of substring in string 
        occurrences = re.finditer(word, line) 
        
        # using reduce() to get start indices of all occurrences 
        res = reduce(lambda x, y: x + [y.start()], occurrences, []) 
        if res != []:
            if word not in matches.keys():
                matches[word] = []

            for item in res:
                matches[word].append(item)

    return matches

def extract_text_calibration_values(input):
    values = []

    for line in input:
        results = find_text(line)
        values.append(results)
        
    return values

def combine_values(numerical_values, text_values):
    values = []

    for x in range(0, len(numerical_values)):
        values.append([])

        for item in numerical_values[x]:
            for value in numerical_values[x][item]:
                values[x].append([item, value])
        
        for item in text_values[x]:
            for value in text_values[x][item]:
                values[x].append([item, value])

    return values

def order_values(values):
    sorted_values = []

    for line in values:
        sorted_values.append(sorted(line, key=lambda x: x[1])) # sort 2-dimensional list by 2nd index => sort on y for [[a, y], [b, y], [c, y]]

    return sorted_values

def convert_to_strings(input):
    values = []

    try:
        for x, line in enumerate(input):
            values.append([])
            for item in line:
                if item[0] in digits:
                    values[x].append(int(item[0]))
                elif item[0] in words:
                    values[x].append(int(word_conversions[item[0]]))
                else:
                    raise Exception
    except Exception:
        print("Unexpected value")

    return values

def combine_first_and_last_digit(values):
    numbers = []

    for line in values:
        numbers.append(int(f"{line[0]}{line[-1]}"))

    return numbers

def sum_and_print_values(values):
    sum = 0

    for value in values:
        sum += value

    print(f"SUM: {sum}")


if __name__ == '__main__':
    file = f'{ABSOLUTE_PATH}/advent_data_{DAY}.txt'
    #file = f'{ABSOLUTE_PATH}/example_advent_data_{DAY}.txt'
    
    input = get_input(file)

    numerical_values = extract_numerical_calibration_values(input)
    text_values = extract_text_calibration_values(input)

    values = combine_values(numerical_values, text_values)
    values = order_values(values)

    values = convert_to_strings(values)
    values = combine_first_and_last_digit(values)
    sum = sum_and_print_values(values)