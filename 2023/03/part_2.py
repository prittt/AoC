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

    # charset = {'#', '=', '-', '/', '*', '&', '+', '%', '$',  '@'}
    
    dict = {}
    r = 0
    while r < len(data):
        line = data[r]
        c = 0
        while c < len(line):
            num = 0
            if line[c].isdigit():
                min_col = c
            while c < len(line) and line[c].isdigit():
                num = num * 10 + int(line[c])
                max_col = c
                c += 1
            
            if num != 0:
                prev_line = data[r-1] if r > 0 else ""
                next_line = data[r+1] if r + 1 < len(data) else ""
                
                prev_line = prev_line[max(0, min_col - 1) : max_col + 2]
                next_line = next_line[max(0, min_col - 1) : max_col + 2]

                prev_c = line[min_col - 1] if min_col > 0 else ""
                next_c = line[max_col + 1] if max_col + 1 < len(line) else ""

                char = "*"
                if char == prev_c: 
                    dict[(r, min_col - 1)] =  dict.get((r, min_col - 1), []) + [num]
                if char == next_c: 
                    dict[(r, max_col + 1)] =  dict.get((r, max_col + 1), []) + [num]
                
                min_col = min_col - 1 if min_col > 0 else 0
                if char in prev_line:
                    dict[(r-1, min_col + prev_line.index(char))] =  dict.get((r-1, min_col + prev_line.index(char)), []) + [num]    
                
                if char in next_line:
                    dict[(r+1, min_col + next_line.index(char))] =  dict.get((r+1, min_col + next_line.index(char)), []) + [num]
                
                # for char in charset: 
                #     if char in prev_line or char in next_line or char == prev_c or char == next_c:
                #         res += num
                #         break

            c += 1
        r += 1
        
    for value in dict.values():
        if len(value) == 2:
            res += value[0] * value[1]

    return res

input_file = os.path.join("2023", os.path.normpath(__file__).split(os.sep)[-2], "input.txt")
with open(input_file) as f:
    example = False
    data = f.read().splitlines()
#     data = """467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598..""".split("\n"); example = True
    print(green(f"DAY {f.name.split(os.sep)[1]}.",  ["bold"]),
          "Running", red(f"{os.path.basename(__file__)}"), "on",
          blue(f"{"example" if example else "real input"}"), "file:")
    res = do(data)  
    print("Result should be (🤞):", res)