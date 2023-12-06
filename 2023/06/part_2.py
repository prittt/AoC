import sys
import sys
import os
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

with open("2023/06/input.txt") as f:
    data = f.read().splitlines()
#     data = """Time:      71530
# Distance:  940200""".split("\n")
    res = do(data)  
    print("Result should be (🤞):", res)
