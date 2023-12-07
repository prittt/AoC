import sys
import os
from simple_colors import *
from pathlib import Path
parent_dir = os.path.dirname(Path(os.path.abspath(__file__)).parent)
sys.path.append(parent_dir)
import utils

@utils.time_decorator
def do(data):
    
    time = data[0][10:].split()
    distance = data[1][10:].split()

    wins = [0] * len(time)
    for i, (t, d) in enumerate(zip(time,distance)):
        for j in range(1, int(t)):
            if j * (int(t) - j) > int(d):
                wins[i] += 1 

    res = 1
    for w in wins:
        res*=w

    return res

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