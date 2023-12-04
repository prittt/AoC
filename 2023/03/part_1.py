def do(data):
    res = 0

    charset = {'#', '=', '-', '/', '*', '&', '+', '%', '$',  '@'}
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

                for char in charset: 
                    if char in prev_line or char in next_line or char == prev_c or char == next_c:
                        res += num
                        break

            c += 1
        r += 1
        
    return res


with open('2023/03/input.txt') as f:
    data = f.read().splitlines()

    # charset = set(data)
    # print(charset)
    
#     data = """467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598..""".split("\n")
    res = do(data)
    print("Result should be (🤞):", res)
