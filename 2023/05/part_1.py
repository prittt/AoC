
import sys
import os
from simple_colors import *
from pathlib import Path
parent_dir = os.path.dirname(Path(os.path.abspath(__file__)).parent)
sys.path.append(parent_dir)
import utils


def get_maps(data):
    data = data[3:]
    maps = []
    curr_map = []
    i = 0
    while i < len(data):
        line = data[i]
        if line == "":
            maps.append(curr_map)
            curr_map = []
            i+=1
        else:
            curr_map.append(line.split())
        i+=1
    maps.append(curr_map)
    return maps

@utils.time_decorator
def do(data):
    
    seeds = data[0].split(":")[1].split()
    maps = get_maps(data)
    
    min_pos = sys.maxsize
    i = 0
    while i < len(seeds):
        seed = int(seeds[i])
        for cur_map in maps:
            for x in cur_map:
                if seed >= int(x[1]) and seed < int(x[2]) + int(x[1]):
                    seed = seed - int(x[1]) + int(x[0])
                    break
        
        if seed < min_pos:
            min_pos = seed
        i += 1
        # print(i)
    
    return min_pos


input_file = os.path.join("2023", os.path.normpath(__file__).split(os.sep)[-2], "input.txt")
with open(input_file) as f:
    example = False
    data = f.read().splitlines()
#     data = """seeds: 79 14 55 13

# seed-to-soil map:
# 50 98 2
# 52 50 48

# soil-to-fertilizer map:
# 0 15 37
# 37 52 2
# 39 0 15

# fertilizer-to-water map:
# 49 53 8
# 0 11 42
# 42 0 7
# 57 7 4

# water-to-light map:
# 88 18 7
# 18 25 70

# light-to-temperature map:
# 45 77 23
# 81 45 19
# 68 64 13

# temperature-to-humidity map:
# 0 69 1
# 1 0 69

# humidity-to-location map:
# 60 56 37
# 56 93 4""".split("\n"); example = True
    print(green(f"DAY {f.name.split(os.sep)[1]}.",  ["bold"]),
          "Running", red(f"{os.path.basename(__file__)}"), "on",
          blue(f"{"example" if example else "real input"}"), "file:")
    res = do(data)  
    print("Result should be (🤞):", res)
