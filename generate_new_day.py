import os

ABSOLUTE_PATH = os.path.dirname(__file__)
DAY = 13

file = f'{ABSOLUTE_PATH}\\advent_data_{DAY}.txt'
example_file = f'{ABSOLUTE_PATH}\\example_advent_data_{DAY}.txt'

new_file = []
with open(f"{ABSOLUTE_PATH}\\new_day.txt", "r") as infile:
    for line in infile:
        new_file.append(line)

with open(f"{ABSOLUTE_PATH}\\advent_{DAY}.py", "w") as outfile:
    for line in new_file:
        outfile.write(line)

new_file = open(file, "w")
new_file.close()

example = open(example_file, "w")
example.close()