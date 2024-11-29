import os

ABSOLUTE_PATH = os.path.dirname(__file__)

day = 5

while os.path.exists(f"{ABSOLUTE_PATH}/advent_{day}_A.py"):
    day += 1

new_file_text = []

with open(f"{ABSOLUTE_PATH}/advent_{day - 1}_A.py", "r") as infile:
    for line in infile:
        new_file_text.append(line)

file = f"{ABSOLUTE_PATH}/advent_{day - 1}_B.py"

with open(file, "w") as outfile:
    for line in new_file_text:
        outfile.write(line)

print(f"\n[COMPLETE] Day {day - 1}B generated.")