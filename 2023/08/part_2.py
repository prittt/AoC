import sys
import os
from simple_colors import *
from pathlib import Path
parent_dir = os.path.dirname(Path(os.path.abspath(__file__)).parent)
sys.path.append(parent_dir)
import utils
from collections import defaultdict, Counter
import math as m

@utils.time_decorator
def do(data):

    instructions = data[0]

    map = {}
    for line in data[2:]:
        map[line[:3]] = (line[7:10], line[12:15]) 
    
    count = 0
    i = 0
    instruction_len = len(instructions) 
    nexts = []
    for k, v in map.items():
        if k.endswith("A"):
            nexts.append(k)

    steps = {}
    while True:
        for j, next in enumerate(nexts):
            # Before submissions
            # if i >= instruction_len:
            #     i = 0
            # instruction = instructions[i]

            # After submissions
            instruction = instructions[i%instruction_len]
            if instruction == "R":
                nexts[j] = map[next][1]
            elif instruction == "L":
                nexts[j] = map[next][0]
            else:
                # After submissions
                print("ERROR")
                exit()
            
            if nexts[j].endswith("Z"):
              steps[j] = count + 1 # Number of steps to reach the Z in the jth path

            if len(steps) == len(nexts):
                # Here I have all the information about the number of steps taken by each path to reach the Z, so I can "combine" them by 
                # calculating the LCM:
                # https://en.wikipedia.org/wiki/Least_common_multiple#:~:text=In%20arithmetic%20and%20number%20theory,by%20both%20a%20and%20b.
                
                # Before submissions
                # res = 1
                # for k, v in steps.items():
                #     res = (res*v) // m.gcd(res, v)

                # After submissions
                res = m.lcm(*steps.values())

                return res 
              
        i+=1
        count += 1 # Using the %, count becomes absolutely useless and always equal to i. It can be safely removed.

    return count

input_file = os.path.join("2023", os.path.normpath(__file__).split(os.sep)[-2], "input.txt")
with open(input_file) as f:
    example = False
    data = f.read().splitlines()
#     data = """LR

# 11A = (11B, XXX)
# 11B = (XXX, 11Z)
# 11Z = (11B, XXX)
# 22A = (22B, XXX)
# 22B = (22C, 22C)
# 22C = (22Z, 22Z)
# 22Z = (22B, 22B)
# XXX = (XXX, XXX))""".split("\n"); example = True
    print(green(f"DAY {f.name.split(os.sep)[1]}.",  ["bold"]),
          "Running", red(f"{os.path.basename(__file__)}"), "on",
          blue(f"{"example" if example else "real input"}"), "file:")
    res = do(data) 
    print("Result should be (🤞):", res)