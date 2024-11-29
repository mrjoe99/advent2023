import os

ABSOLUTE_PATH = os.path.dirname(__file__)

day = 0

while os.path.exists(f"{ABSOLUTE_PATH}/advent_{day}_A.py"):
    day += 1

file = f"{ABSOLUTE_PATH}/advent_data_{day}.txt"
example_file = f"{ABSOLUTE_PATH}/example_advent_data_{day}.txt"

file = open(file, "w")
file.close()

file = open(example_file, "w")
file.close()

new_day_text = []
with open(f"{ABSOLUTE_PATH}/new_day_A.txt", "r") as infile:
    for line in infile:
        new_day_text.append(line)

file = f"{ABSOLUTE_PATH}/advent_{day}_A.py"

with open(file, "w") as outfile:
    for line in new_day_text:
        outfile.write(line)

print(f"[COMPLETE] Day {day}A generated.")