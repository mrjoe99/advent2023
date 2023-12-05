import os

ABSOLUTE_PATH = os.path.dirname(__file__)
DAY = 1
EXAMPLE = True

def get_input():
    file = ""
    temp = ""

    if EXAMPLE:
        file = f'{ABSOLUTE_PATH}\\example_advent_data_{DAY}.txt'
    else:
        file = f'{ABSOLUTE_PATH}\\advent_data_{DAY}.txt'

    with open(file, 'r') as input:
        temp = []

        for line in input:
            temp.append(line.strip('\n'))

        return temp
    
def extract_numerical_calibration_values(input):
    values = []
    digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    for line in input:
        line_values = []

        for x in range(0, len(line)):
            if line[x] in digits:
                line_values.append([line[x], x]) # [value, starting index]

        values.append(line_values)

    return values

def find_text(line):
    values = []
    current_index = 0
    #iteration = 0

    three_slice = line[current_index: current_index + 3] # 3 letter words: one, two, six
    four_slice = line[current_index: current_index + 4]  # 4 letter words: four, five, nine
    five_slice = line[current_index: current_index + 5]  # 5 letter words: three, seven, eight

    while current_index <= len(line):
        # if iteration > 0:
        #     current_index += 1
        #     iteration = 0
        
            # three_slice = line[current_index: current_index + 3]
            # four_slice = line[current_index: current_index + 4]
            # five_slice = line[current_index: current_index + 5]

        if three_slice == "one": 
            index = line.find("one", current_index)
            #current_index += 3 # (length of the word 'one')

            three_slice = line[current_index: current_index + 3]
            four_slice = line[current_index: current_index + 4]
            five_slice = line[current_index: current_index + 5]

            if index == -1:
                break
            values.append(["1", index])
        elif three_slice == "two":
            index = line.find("two", current_index)
            #current_index += 3 # (length of the word 'two')

            three_slice = line[current_index: current_index + 3]
            four_slice = line[current_index: current_index + 4]
            five_slice = line[current_index: current_index + 5]

            if index == -1:
                break
            values.append(["2", index])
        elif three_slice == "six":
            index = line.find("six", current_index)
            #current_index += 3 # (length of the word 'six')

            three_slice = line[current_index: current_index + 3]
            four_slice = line[current_index: current_index + 4]
            five_slice = line[current_index: current_index + 5]

            if index == -1:
                break
            values.append(["6", index])
        
        if four_slice == "four": 
            index = line.find("four", current_index)
            #current_index += 4 # (length of the word 'four')

            three_slice = line[current_index: current_index + 3]
            four_slice = line[current_index: current_index + 4]
            five_slice = line[current_index: current_index + 5]

            if index == -1:
                break
            values.append(["4", index])
        elif four_slice == "five":
            index = line.find("five", current_index)
            #current_index += 4 # (length of the word 'five')

            three_slice = line[current_index: current_index + 3]
            four_slice = line[current_index: current_index + 4]
            five_slice = line[current_index: current_index + 5]

            if index == -1:
                break
            values.append(["5", index])
        elif four_slice == "nine":
            index = line.find("nine", current_index)
            #current_index += 4 # (length of the word 'nine')

            three_slice = line[current_index: current_index + 3]
            four_slice = line[current_index: current_index + 4]
            five_slice = line[current_index: current_index + 5]

            if index == -1:
                break
            values.append(["9", index])

        if five_slice == "three": 
            index = line.find("three", current_index)
            #current_index += 5 # (length of the word 'three')

            three_slice = line[current_index: current_index + 3]
            four_slice = line[current_index: current_index + 4]
            five_slice = line[current_index: current_index + 5]

            if index == -1:
                break
            values.append(["3", index])
        elif five_slice == "seven":
            index = line.find("seven", current_index)
            #current_index += 5 # (length of the word 'seven')

            three_slice = line[current_index: current_index + 3]
            four_slice = line[current_index: current_index + 4]
            five_slice = line[current_index: current_index + 5]

            if index == -1:
                break
            values.append(["7", index])
        elif five_slice == "eight":
            index = line.find("eight", current_index)
            #current_index += 5 # (length of the word 'eight')

            three_slice = line[current_index: current_index + 3]
            four_slice = line[current_index: current_index + 4]
            five_slice = line[current_index: current_index + 5]

            if index == -1:
                break
            values.append(["8", index])
        
        # if (three_slice != "one" and three_slice != "two" and three_slice != "six" and # nudge 'current_index' forward by 1 if word not matched
        #     four_slice != "four" and four_slice != "five" and four_slice != "nine" and
        #     five_slice != "three" and five_slice != "seven" and five_slice != "eight"):
        #     iteration += 1
        
        current_index += 1

    return values

def extract_text_calibration_values(input):
    values = []

    for line in input:
        results = find_text(line)
        values.append(results)
        
    return values

def combine_values(numerical_values, text_values):
    values = []

    for x in range(0, len(numerical_values)):
        values.append(numerical_values[x])
        values[x].extend(text_values[x])

    return values

def order_values(values):
    sorted_values = []

    for line in values:
        sorted_values.append(sorted(line, key=lambda x: x[1])) # sort 2-dimensional list by 2nd index => sort on y for [[a, y], [b, y], [c, y]]

    return sorted_values

def convert_to_integers(sorted):
    values = []

    for item in sorted:
        values.append(int((item[0][0] + item[len(item) - 1][0])))

    return values

def sum_and_print_values(values):
    sum = int()

    for value in values:
        sum += value

    print(sum)


if __name__ == '__main__':
    input = get_input()

    numerical_values = extract_numerical_calibration_values(input)
    text_values = extract_text_calibration_values(input)

    combined_values = combine_values(numerical_values, text_values)
    ordered_values = order_values(combined_values)

    integer_values = convert_to_integers(ordered_values)
    sum = sum_and_print_values(integer_values)

    print("DEBUG")

# 53587 - too low
# 54494 - too high