# import sys

def do(data):
    
    # Parse data
    time = data[0][10:].strip().replace(" ", "").replace(" ", "").replace(" ", "").replace(" ", "")
    distance = data[1][10:].strip().replace(" ", "").replace(" ", "").replace(" ", "").replace(" ", "")
    print(time, distance)

    time = int(time)
    distance = int(distance)

    # wins = [0] * len(time)
    # for i, (t, d) in enumerate(zip(time,distance)):
    
    wins = 0
    for j in range(time + 1):
        dx = j*(time-j)
        if dx >= distance:
            wins += 1 

    return wins

with open(r"C:\Users\Federico\Desktop\AoC\2023\06\input.txt") as f:
    data = f.read().splitlines()
#     data = """Time:      71530
# Distance:  940200""".split("\n")
    res = do(data)  
    print("Result should be (🤞):", res)
