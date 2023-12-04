def do(data):
    res = 0
    for line in data:
        for c in line:
            if c.isdigit():
                num = int(c)
                break
        for c in reversed(line):
            if c.isdigit():
                num = num * 10 + int(c)
                break
        res += num 
    return res


with open('2023/01/input.txt') as f:
    data = f.read().splitlines()
    res = do(data)
    print("Result should be (🤞):", res)
