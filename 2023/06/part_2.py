import sys
import os
from simple_colors import *
from pathlib import Path
parent_dir = os.path.dirname(Path(os.path.abspath(__file__)).parent)
sys.path.append(parent_dir)
import utils

@utils.time_decorator
def do(data):
    
    # Very bad version for the quick output (my brain was in a hurry, just put some replaces and it will work)
    # I know, I should use regular expressions, but I'm lazy
    # time = data[0][10:].strip().replace(" ", "").replace(" ", "").replace(" ", "").replace(" ", "")
    # distance = data[1][10:].strip().replace(" ", "").replace(" ", "").replace(" ", "").replace(" ", "")

    # Fixed parsing (after the submission)
    time = data[0][10:].split()
    distance = data[1][10:].split()
    
    time = int("".join(time))
    distance = int("".join(distance))
   
    wins = 0
    for j in range(time + 1):
        curr_distance = j*(time - j)
        if curr_distance >= distance:
            wins += 1 

    return wins

input_file = os.path.join("2023", os.path.normpath(__file__).split(os.sep)[-2], "input.txt")
with open(input_file) as f:
    example = False
    data = f.read().splitlines()
#     data = """Time:      7  15   30
# Distance:  9  40  200
# """.split("\n"); example = True
    print(green(f"DAY {f.name.split(os.sep)[1]}.",  ["bold"]),
          "Running", red(f"{os.path.basename(__file__)}"), "on",
          blue(f"{"example" if example else "real input"}"), "file:")
    res = do(data)  
    print("Result should be (🤞):", res)