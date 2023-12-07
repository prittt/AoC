import sys
import os
from simple_colors import *
from pathlib import Path
parent_dir = os.path.dirname(Path(os.path.abspath(__file__)).parent)
sys.path.append(parent_dir)
import utils

@utils.time_decorator
def do(data):
    res = 0
    for line in data:
        curr_sol = 0
        old_line = line
        line = line.strip().split(":")[1]
        line = line.split("|")
        winning_nums = line[0].split()
        my_nums = line[1].split()

        for my_num in my_nums:
            if my_num in winning_nums:
                curr_sol += 1
        
        res += 0 if curr_sol <= 0 else int(2 ** (curr_sol - 1))

    return res


input_file = os.path.join("2023", os.path.normpath(__file__).split(os.sep)[-2], "input.txt")
with open(input_file) as f:
    example = False
    data = f.read().splitlines()
#     data = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
# Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
# Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
# Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
# Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
# Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11""".split("\n"); example = True
    print(green(f"DAY {f.name.split(os.sep)[1]}.",  ["bold"]),
          "Running", red(f"{os.path.basename(__file__)}"), "on",
          blue(f"{"example" if example else "real input"}"), "file:")
    res = do(data)  
    print("Result should be (🤞):", res)
