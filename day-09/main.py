def part1():
    line = ""

    with open("input.txt") as file:
        line = file.readline()

    blocks = []
    block_count = 0

    for i in range(len(line)):
        size = int(line[i])
        if i % 2 == 0:
            blocks.extend([block_count]*size)
            block_count += 1
        else:
            blocks.extend(['.']*size)
    
    start = 0
    end = len(blocks)-1

    while start <= end:
        if blocks[start] != '.':
            start += 1
        elif blocks[end] != '.':
            blocks[start], blocks[end] = blocks[end], '.'
            end -= 1
            start += 1
        else:
            end -= 1
    
    checksum = 0

    for i in range(len(blocks)):
        if blocks[i] != '.':
            checksum += i * blocks[i]
    
    return checksum

def part2():
    line = ""
    with open("input.txt") as file:
        line = file.readline().strip()

    blocks = []
    block_count = 0
    block_map =  {}

    for i in range(len(line)):
        if i % 2 == 0:
            start_index = len(blocks)
            file_size = int(line[i])
            blocks.extend([block_count]*file_size)
            block_map[block_count] = (start_index, file_size)
            block_count += 1
        else:
            free_size = int(line[i])
            blocks.extend(['.']*free_size)

    for id in reversed(list(block_map.keys())):
        current_index, current_size = block_map[id]

        free_index, free_size = 0, 0
        can_move = True
        
        while free_size < current_size and can_move:
            if free_index >= current_index:
                can_move = False

            if blocks[free_index] != '.':
                free_index += 1
                free_size = 0
            elif blocks[free_index + free_size] == '.':
                free_size += 1
            else:
                free_index = free_index + free_size
                free_size = 0
        
        if can_move:
            for i in range(current_size):
                blocks[free_index + i] = id
                blocks[current_index + i] = '.'
    
    checksum = 0

    for i in range(len(blocks)):
        if blocks[i] != '.':
            checksum += i * blocks[i]
    
    return checksum

if __name__ == "__main__":
    print("Day 9, Part 1: " + str(part1()))
    print("Day 9, Part 2: " + str(part2()))