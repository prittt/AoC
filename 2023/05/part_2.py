
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

def do(data):
    
    seeds = data[0].split(":")[1].split()

    min_pos = sys.maxsize
    i = 0
    seed_ranges = {}
    while i < len(seeds):
        start = int(seeds[i])
        end = int(seeds[i]) + int(seeds[i + 1])
        seed_ranges[(start, end)] = (start, end)
        i += 2

    # seed = int(seed)
    mappings = get_maps(data)
    # mappings = [seed_to_soil_map, soil_to_fertilizer_map, fertilizer_to_water_map, water_to_ligh_map, light_to_temp_map, temperature_to_humidity_map, humidity_to_location_map]
    mappings_name = ["seed_to_soil_map", "soil_to_fertilizer_map", "fertilizer_to_water_map", "water_to_ligh_map", "light_to_temp_map", "temperature_to_humidity_map", "humidity_to_location_map"]
    for k in seed_ranges:
        ranges = {k: k}
        for m,name in zip(mappings, mappings_name):
            updated_ranges = {}
            not_updated_ranges = {}
            # print(name)
            for x in m: # qui itero tu tutti i mapping dell'm corrente (seed to soil, poi soil to fertilizer, etc.)
                source_start = int(x[1])
                source_end = int(x[2]) + int(x[1])

                destination_start = int(x[0])
                destination_end = int(x[0]) + int(x[2])
                
                for start, end in ranges.values():
                    if end < source_start or start > source_end:
                        # just keep the same range 
                        # not_updated_ranges.pop(0)
                        not_updated_ranges[(start, end)] = (start, end)
                    else:
                        if start < source_start:
                            not_updated_ranges[(start, source_start - 1)] = (start, source_start - 1)  # il primo pezzo rimane così come era
                            
                            if end > source_end:
                                # converto fino a destination end
                                updated_ranges[(destination_start, destination_end)] = (destination_start, destination_end)
                                # e lascio il resto così com'era
                                not_updated_ranges[(source_end, end)] = (source_end, end)
                            else:
                                # converto fino a end
                                updated_ranges[(destination_start, end - source_start + destination_start)] = (destination_start, end - source_start + destination_start)
                        else:
                            if end > source_end:
                                # converto fino a destination end
                                updated_ranges[(destination_start + start -source_start, destination_end)] = (destination_start + start -source_start, destination_end)
                                # e lascio il resto così com'era
                                not_updated_ranges[(source_end, end)] = (source_end, end)
                            else:
                                # sono tutto dentro
                                updated_ranges[(destination_start + start -source_start, end - source_start + destination_start)] = (destination_start + start -source_start, end - source_start + destination_start)
                        not_updated_ranges.pop((start, end), None)
                ranges = not_updated_ranges.copy()
            
            ranges = updated_ranges.copy()
            ranges.update(not_updated_ranges.copy())

        for r in ranges:
            if r[0] < min_pos:
                min_pos = r[0]
            
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