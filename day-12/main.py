from collections import deque

directions = {
    (1, 0) : 'v',
    (0, 1) : '<',
    (-1, 0): '^',
    (0, -1): '>'
}

def part1():
    grid = []

    with open("input.txt") as file:
        grid = [list(line.strip()) for line in file]

    visited = set([])

    def find_plot(x, y):
        current_plot = deque([])
        current_plot.append((x,y))

        plot_size = 0
        plot_perimeter = 0

        while len(current_plot)>0:
            c_x, c_y = current_plot.popleft()

            if (c_x, c_y) in visited:
                continue

            plot_size += 1
            visited.add((c_x, c_y))

            for coordinates in directions.keys():
                n_x, n_y = c_x + coordinates[0], c_y + coordinates[1]
                
                if n_x < 0 or n_x >= len(grid[0]) or n_y < 0 or n_y >= len(grid):
                    plot_perimeter += 1
                    continue

                if grid[c_y][c_x] != grid[n_y][n_x]:
                    plot_perimeter += 1
                    continue

                if (n_x, n_y) in visited:
                    continue

                current_plot.append((n_x, n_y))
        return plot_size * plot_perimeter
    
    total_price = 0

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] not in visited:
                total_price += find_plot(x, y)

    return total_price

def part2():
        grid = []

        with open("input.txt") as file:
            grid = [list(line.strip()) for line in file]

        visited = set([])

        def find_plot(x, y):
            current_plot = deque([])
            current_plot.append((x,y))

            plot_size = 0
            plot_edges = set([])

            while len(current_plot)>0:
                c_x, c_y = current_plot.popleft()

                if (c_x, c_y) in visited:
                    continue

                plot_size += 1
                visited.add((c_x, c_y))

                for coordinates, direction in directions.items():
                    n_x, n_y = c_x + coordinates[0], c_y + coordinates[1]
                    
                    if n_x < 0 or n_x >= len(grid[0]) or n_y < 0 or n_y >= len(grid):
                        plot_edges.add((n_x, n_y, direction))
                        continue

                    if grid[c_y][c_x] != grid[n_y][n_x]:
                        plot_edges.add((n_x, n_y, direction))
                        continue

                    if (n_x, n_y) in visited:
                        continue

                    current_plot.append((n_x, n_y))
            return plot_size, plot_edges

        def find_edges(plot_edges):
            plot_edges = deque(plot_edges)

            plot_perimeter = 0

            while len(plot_edges) > 0:
                c_x, c_y, c_d = plot_edges.popleft()
                plot_perimeter += 1
                if c_d == '>' or c_d == '<':
                    l_x, l_y, l_d = c_x - 1, c_y, c_d

                    while (l_x, l_y, l_d) in plot_edges:
                        plot_edges.remove((l_x, l_y, l_d))
                        l_x = l_x - 1
                    
                    r_x, r_y, r_d = c_x + 1, c_y, c_d
                    while (r_x, r_y, r_d) in plot_edges:
                        plot_edges.remove((r_x, r_y, r_d))
                        r_x = r_x + 1

                elif c_d == '^' or c_d == 'v':
                    u_x, u_y, u_d = c_x, c_y - 1, c_d
                    while (u_x, u_y, u_d) in plot_edges:
                        plot_edges.remove((u_x, u_y, u_d))
                        u_y = u_y - 1

                    d_x, d_y, d_d = c_x, c_y + 1, c_d
                    while (d_x, d_y, d_d) in plot_edges:
                        plot_edges.remove((d_x, d_y, d_d))
                        d_y = d_y + 1
            return plot_perimeter

        total_price = 0

        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] not in visited:
                    plot_size, plot_edges = find_plot(x, y)
                    plot_perimeter = find_edges(plot_edges)
                    total_price += plot_size * plot_perimeter

        return total_price


if __name__ == "__main__":
    print("Day 12, Part 1: " + str(part1()))
    print("Day 12, Part 2: " + str(part2()))