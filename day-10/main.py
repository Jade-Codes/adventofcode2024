directions = [
    (0,1),
    (1,0),
    (0,-1),
    (-1,0)
]

def part1():
    grid = []

    with open("input.txt") as file:
        grid = [list(line.strip()) for line in file]

    valid_trailheads = set([])

    def find_paths(f_x, f_y, c_x, c_y, c_v):
        if int(grid[c_y][c_x]) == 9:
            valid_trailheads.add((f_x, f_y, c_x, c_y))
            return
        
        for direction in directions:
            n_x = c_x + direction[0]
            n_y = c_y + direction[1]
            n_v = c_v + 1

            if n_x < 0 or n_x >= len(grid[0]) or n_y < 0 or n_y >= len(grid):
                continue

            if grid[n_y][n_x] == '.':
                continue
            
            if int(grid[n_y][n_x]) == n_v:
                find_paths(f_x, f_y, n_x, n_y, n_v)

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == '0':
                find_paths(x, y, x, y, 0)

    return len(valid_trailheads)

def part2():
    grid = []

    with open("input.txt") as file:
        grid = [list(line.strip()) for line in file]

    valid_paths = []

    def find_paths(c_x, c_y, c_v, path):
        if int(grid[c_y][c_x]) == 9:
            valid_paths.append(path)
            return
        
        for direction in directions:
            n_x = c_x + direction[0]
            n_y = c_y + direction[1]
            n_v = c_v + 1

            if n_x < 0 or n_x >= len(grid[0]) or n_y < 0 or n_y >= len(grid):
                continue

            if grid[n_y][n_x] == '.':
                continue
            
            if int(grid[n_y][n_x]) == n_v:
                path.append((n_x, n_y))
                find_paths(n_x, n_y, n_v, path)

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == '0':
                path = [(x, y)]
                find_paths(x, y, 0, path)

    return len(valid_paths)

if __name__ == "__main__":
    print("Day 10, Part 1: " + str(part1()))
    print("Day 10, Part 2: " + str(part2()))