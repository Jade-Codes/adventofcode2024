from functools import cache

def get_current_stones(stone):
    if stone == 0:
        return [1]
    if len(str(stone)) % 2 == 0:
        stone_str = str(stone)
        stone_len = len(str(stone))
        return [int(stone_str[:(stone_len//2)]), int(stone_str[(stone_len//2):])]
    return [stone * 2024]

@cache
def count_stones(stone, blink):
    if blink == 0:
        return 1
    
    total_stones = 0
    for current_stone in get_current_stones(stone):
        total_stones += count_stones(current_stone, blink-1)
    
    return total_stones

def part1():
    line = ""

    with open("input.txt") as file:
        line = file.readline()

    stones = list(map(int, line.split(' ')))

    total_count = 0
    for stone in stones:
        total_count += count_stones(stone, 25)

    return total_count

def part2():
    line = ""

    with open("input.txt") as file:
        line = file.readline()

    stones = list(map(int, line.split(' ')))

    total_count = 0

    for stone in stones:
        total_count += count_stones(stone, 75)

    return total_count
        
if __name__ == "__main__":
    print("Day 11, Part 1: " + str(part1()))
    print("Day 11, Part 2: " + str(part2()))