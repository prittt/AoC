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
    for i, line in enumerate(data, 1):
        best_set = {"green":0, "red": 0, "blue": 0}
        old_line = line
        sets = line.split(":")[1].split(";")
        for s in sets:
            colors = s.split(",")
            for c in colors:
                for best in best_set.keys():
                    if best in c:
                        best_set[best] = max(best_set[best], int(c.replace(best, "")))
                        break

        if best_set["red"] <= 12 and best_set["green"] <= 13 and best_set["blue"] <= 14:
            res += i

    return res


input_file = os.path.join("2023", os.path.normpath(__file__).split(os.sep)[-2], "input.txt")
with open(input_file) as f:
    example = False
    data = f.read().splitlines()
#     data = """""".split("\n"); example = True
    print(green(f"DAY {f.name.split(os.sep)[1]}.",  ["bold"]),
          "Running", red(f"{os.path.basename(__file__)}"), "on",
          blue(f"{"example" if example else "real input"}"), "file:")
    res = do(data)  
    print("Result should be (🤞):", res)