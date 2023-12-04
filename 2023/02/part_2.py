import sys

def do(data):
    res = 0
    for i, line in enumerate(data, 1):
        best_set = {"green": 0, "red": 0, "blue": 0}
        old_line = line
        sets = line.split(":")[1].split(";")
        for s in sets:
            colors = s.split(",")
            for c in colors:
                for best in best_set.keys():
                    if best in c:
                        best_set[best] = max(best_set[best], int(c.replace(best, "")))
                        break

        res += best_set["red"] * best_set["green"] * best_set["blue"]
        
    return res


with open('2023/02/input.txt') as f:
    data = f.read().splitlines()
    res = do(data)
    print("Result should be (🤞):", res)
