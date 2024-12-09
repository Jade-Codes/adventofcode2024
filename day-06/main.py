directions = {
    'N': (0, -1),
    'E': (1, 0),
    'S': (0, 1),
    'W': (-1, 0)
}

rotate = {
    'N' : 'E',
    'E' : 'S',
    'S' : 'W',
    'W' : 'N'
}

def part1():
    lab = []

    with open("input.txt") as file:
        lab = [list(line.strip()) for line in file]

    (current_x, current_y) = (-1,-1)
    current_direction = 'N'
    distinct_positions = 0

    for y in range(len(lab)):
        for x in range(len(lab[0])):
            if lab[y][x] == '^':
                (current_x, current_y) = (x, y)
                distinct_positions += 1
                lab[y][x] = 'X'
                break
        
        if (current_x, current_y) != (-1,-1):
            break
    
    exited = False
    while not exited:
        (next_x, next_y) = (current_x + directions[current_direction][0], current_y + directions[current_direction][1])

        if next_x < 0 or next_x >= len(lab[0]) or next_y < 0 or next_y >= len(lab):
            exited = True
        elif lab[next_y][next_x] == '#':
            current_direction = rotate[current_direction]
        elif lab[next_y][next_x] == '.':
            distinct_positions += 1
            (current_x, current_y) = (next_x, next_y)
            lab[current_y][current_x] = 'X'
        elif lab[next_y][next_x] == 'X':           
            (current_x, current_y) = (next_x, next_y)

    return distinct_positions

def part2():
    lab = []

    with open("input.txt") as file:
        lab = [list(line.strip()) for line in file]

    (start_x, start_y) = (-1,-1)
    (current_x, current_y) = (-1,-1)

    start_direction = 'N'
    current_direction = 'N'
    distinct_positions = 0

    for y in range(len(lab)):
        for x in range(len(lab[0])):
            if lab[y][x] == '^':
                (start_x, start_y) = (x, y)
                (current_x, current_y) = (x, y)
                distinct_positions += 1
                lab[y][x] = '.'
                break
    
    visited_positions = set()
    exited = False
    while not exited:
        (next_x, next_y) = (current_x + directions[current_direction][0], current_y + directions[current_direction][1])

        if next_x < 0 or next_x >= len(lab[0]) or next_y < 0 or next_y >= len(lab):
            exited = True
        elif lab[next_y][next_x] == '#':
            current_direction = rotate[current_direction]
        elif lab[next_y][next_x] == '.':
            distinct_positions += 1
            (current_x, current_y) = (next_x, next_y)
        
        if (current_x, current_y) != (start_x, start_y):
            visited_positions.add((current_x, current_y))

    obstructions = 0

    for visited_position in visited_positions:
        (current_x, current_y) = (start_x, start_y)
        current_direction = start_direction
        exited = False
        current_visited_positions = set()
        lab[visited_position[1]][visited_position[0]] = '#'

        while not exited:
            (next_x, next_y) = (current_x + directions[current_direction][0], current_y + directions[current_direction][1])

            if (next_x, next_y, current_direction) in current_visited_positions:
                obstructions += 1
                exited = True
            elif next_x < 0 or next_x >= len(lab[0]) or next_y < 0 or next_y >= len(lab):
                exited = True
            elif lab[next_y][next_x] == '#':
                current_direction = rotate[current_direction]
            elif lab[next_y][next_x] == '.':
                distinct_positions += 1
                (current_x, current_y) = (next_x, next_y)
            
            if (current_x, current_y) != (start_x, start_y):
                current_visited_positions.add((current_x, current_y, current_direction))
            
        lab[visited_position[1]][visited_position[0]] = '.'
    return obstructions

if __name__ == "__main__":
    print("Day 6, Part 1: " + str(part1()))
    print("Day 6, Part 2: " + str(part2()))