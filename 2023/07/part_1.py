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
    return res

with open("2023/07/input.txt") as f:
    print(red("Part 1:"))
    data = f.read().splitlines()
#     data = """""".split("\n")
    res = do(data)  
    print("Result should be (🤞):", res)
