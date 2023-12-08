import sys
import os
from simple_colors import *
from pathlib import Path
parent_dir = os.path.dirname(Path(os.path.abspath(__file__)).parent)
sys.path.append(parent_dir)
import utils
from collections import defaultdict, Counter

@utils.time_decorator
def do(data):

    instructions = data[0]

    map = {}
    for line in data[2:]:
        map[line[:3]] = (line[7:10], line[12:15]) 
    
    count = 0
    i = 0
    instruction_len = len(instructions) 
    next = "AAA"
    while next != "ZZZ":
        # Before submissions
        # if i >= instruction_len:
        #     i = 0
        # instruction = instructions[i]

        # After submissions
        instruction = instructions[i%instruction_len]
        if instruction == "R":
            next = map[next][1]
        elif instruction == "L":
            next = map[next][0]
        else:
            # After submissions
            print("ERROR")
            exit()
        i+=1
        count += 1  # Using the %, count becomes absolutely useless and always equal to i. It can be safely removed.

    return count

input_file = os.path.join("2023", os.path.normpath(__file__).split(os.sep)[-2], "input.txt")
with open(input_file) as f:
    example = False
    data = f.read().splitlines()
#     data = """RL

# AAA = (BBB, CCC)
# BBB = (DDD, EEE)
# CCC = (ZZZ, GGG)
# DDD = (DDD, DDD)
# EEE = (EEE, EEE)
# GGG = (GGG, GGG)
# ZZZ = (ZZZ, ZZZ)""".split("\n"); example = True
#     data = """LLR

# AAA = (BBB, BBB)
# BBB = (AAA, ZZZ)
# ZZZ = (ZZZ, ZZZ)""".split("\n"); example = True
    print(green(f"DAY {f.name.split(os.sep)[1]}.",  ["bold"]),
          "Running", red(f"{os.path.basename(__file__)}"), "on",
          blue(f"{"example" if example else "real input"}"), "file:")
    res = do(data) 
    print("Result should be (🤞):", res)