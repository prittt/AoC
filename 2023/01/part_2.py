def do(data):
    numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    values = {"one" : 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8 , "nine": 9, "1": 1, "2": 2, "3":3 , "4":4, "5":5, "6":6, "7":7, "8":8, "9":9}
    res = 0
    for line in data:
        min_pos = len(line)
        max_pos = 0
        for x in numbers:
            min_pos = min(min_pos, line.find(x) if line.find(x) != -1 else len(line))
            max_pos = max(max_pos, line.rfind(x))            
        
        num = 0
        first = line[min_pos:]
        last = line[max_pos:]
        for x in numbers:
            if first.startswith(x):
                num += values[x] * 10
            if last.startswith(x):
                num += values[x]
        
        res += num
    return res

with open('2023/01/input.txt') as f:
    data = f.read().splitlines()
    res = do(data)
    print("Result should be (🤞):", res)
