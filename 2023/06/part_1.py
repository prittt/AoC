
import sys

def do(data):
    
    # Parse data
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

with open(r"C:\Users\Federico\Desktop\AoC\2023\06\input.txt") as f:
    data = f.read().splitlines()
#     data = """Time:      7  15   30
# Distance:  9  40  200
# """.split("\n")
    res = do(data)  
    print("Result should be (🤞):", res)
