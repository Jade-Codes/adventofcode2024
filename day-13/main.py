import re    

def cramers_rule(a_x, b_x, p_x, a_y, b_y, p_y):
    det = a_x*b_y - b_x*a_y
    if det == 0:
        return (None, None)
    
    x = (p_x*b_y - b_x*p_y)/det
    y = (a_x*p_y - p_x*a_y)/det

    if x.is_integer() and y.is_integer():
        return (x, y)
    return (None, None)

def part1():
    lines = []

    with open("input.txt") as file:
        lines = file.readlines()
    
    a_x, a_y = 0, 0
    b_x, b_y = 0, 0
    p_x, p_y = 0, 0

    total_tokens = 0

    for line in lines:
        numbers = list(map(int, re.findall("\d+", line)))
        if 'Button A' in line:
            a_x, a_y = numbers[0], numbers[1]
        elif 'Button B' in line:
            b_x, b_y = numbers[0], numbers[1]
        elif 'Prize' in line:
            p_x, p_y = numbers[0], numbers[1]

            a, b = cramers_rule(a_x, b_x, p_x, a_y, b_y, p_y)
            if a is not None and b is not None:
                if a <= 100 and b <= 100:
                    total_tokens += int(a*3 + b)
        
    return total_tokens

def part2():
    lines = []

    with open("input.txt") as file:
        lines = file.readlines()
    
    a_x, a_y = 0, 0
    b_x, b_y = 0, 0
    p_x, p_y = 0, 0

    total_tokens = 0

    for line in lines:
        numbers = list(map(int, re.findall("\d+", line)))
        if 'Button A' in line:
            a_x, a_y = numbers[0], numbers[1]
        elif 'Button B' in line:
            b_x, b_y = numbers[0], numbers[1]
        elif 'Prize' in line:
            p_x, p_y = 10000000000000 + numbers[0], 10000000000000 + numbers[1]

            a, b = cramers_rule(a_x, b_x, p_x, a_y, b_y, p_y)
            if a is not None and b is not None:
                total_tokens += int(a*3 + b)
        
    return total_tokens
    
if __name__ == "__main__":
    print("Day 13, Part 1: " + str(part1()))
    print("Day 13, Part 2: " + str(part2()))