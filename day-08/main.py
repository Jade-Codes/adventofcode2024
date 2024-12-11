def part1():
    grid = []

    with open("input.txt") as file:
        grid = file.readlines()

    freq_map = {}
    antinodes = set([])

    for y in range(len(grid)):
        for x in range(len(grid[0].strip())):
            freq = grid[y][x]
            if freq != '.':
                freq_map[freq] = freq_map.get(freq, [])
                freq_map[freq].append((x, y))
    
    for freq, pos in freq_map.items():
        for i in range(len(pos)):
            for j in range(i+1, len(pos)):
                x2, y2 = pos[j][0], pos[j][1]
                x1, y1 = pos[i][0], pos[i][1]
                dx, dy = x2 - x1, y2 - y1

                fx, fy = x1 - dx, y1 - dy
                sx, sy = x2 + dx, y2 + dy

                if fx >= 0 and fx < len(grid[0].strip()) and fy >= 0 and fy < len(grid):
                    antinodes.add((fx, fy))
                
                if sx >= 0 and sx < len(grid[0].strip()) and sy >= 0 and sy < len(grid):
                    antinodes.add((sx, sy))
    
    return len(antinodes)

def part2():
    grid = []

    with open("input.txt") as file:
        grid = [list(line.strip()) for line in file]
    
    freq_map = {}
    antinodes = set([])

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            freq = grid[y][x]
            if freq != '.':
                freq_map[freq] = freq_map.get(freq, [])
                freq_map[freq].append((x, y))
    
    for freq, pos in freq_map.items():
        for i in range(len(pos)):
            for j in range(i+1, len(pos)):
                x2, y2 = pos[j][0], pos[j][1]
                x1, y1 = pos[i][0], pos[i][1]
                dx, dy = x2 - x1, y2 - y1

                fx, fy = x1 - dx, y1 - dy
                sx, sy = x2 + dx, y2 + dy

                antinodes.add((pos[i][0], pos[i][1]))
                antinodes.add((pos[j][0], pos[j][1]))

                while fx >= 0 and fx < len(grid[0]) and fy >= 0 and fy < len(grid):
                    antinodes.add((fx, fy))
                    fx, fy = fx - dx, fy - dy

                while sx >= 0 and sx < len(grid[0]) and sy >= 0 and sy < len(grid):
                    antinodes.add((sx, sy))
                    sx, sy = sx + dx, sy + dy

    return len(antinodes)

if __name__ == "__main__":
    print("Day 8, Part 1: " + str(part1()))
    print("Day 8, Part 2: " + str(part2()))