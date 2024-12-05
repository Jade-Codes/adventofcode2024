directions = {
    (-1,0),
    (-1,-1),
    (-1,1),
    (0,-1),
    (0,1),
    (1,-1),
    (1,0),
    (1,1)
}

def can_move(word_search, x, y, direction):
    can_move_x = x + direction[1]*3
    can_move_y = y + direction[0]*3

    if can_move_y < 0 or can_move_y >= len(word_search):
        return False
    
    if can_move_x < 0 or can_move_x >= len(word_search[0]):
        return False

    return True

def is_xmas(word_search, x, y, direction):
    if word_search[y + direction[0]*1][x + direction[1]*1] != 'M':
        return False
    
    if word_search[y + direction[0]*2][x + direction[1]*2] != 'A':
        return False

    if word_search[y + direction[0]*3][x + direction[1]*3] != 'S':
        return False
    
    return True

def part1():
    word_search = []
    with open("input.txt") as file:
        word_search = file.readlines()

    count = 0 

    for y in range(len(word_search)):
        for x in range(len(word_search[0].strip())):
            if word_search[y][x] == 'X':
                for direction in directions:
                    if can_move(word_search, x, y, direction) and is_xmas(word_search, x, y, direction):
                        count += 1
    
    return count


def part2():
    word_search = []
    with open("input.txt") as file:
        word_search = file.readlines()

    count = 0
    
    for y in range(1, len(word_search)-1):
        for x in range(1, len(word_search[0].strip())-1):
             if word_search[y][x] == 'A':
                 if ((word_search[y-1][x-1] == 'M' and word_search[y+1][x+1] == 'S') or \
                    (word_search[y-1][x-1] == 'S' and word_search[y+1][x+1] == 'M')) and \
                    ((word_search[y-1][x+1] == 'M' and word_search[y+1][x-1] == 'S') or \
                    (word_search[y-1][x+1] == 'S' and word_search[y+1][x-1] == 'M')):
                    count +=1

    return count    

if __name__ == "__main__":
    print("Day 4, Part 1: " + str(part1()))
    print("Day 4, Part 2: " + str(part2()))