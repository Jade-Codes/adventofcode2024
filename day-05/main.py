def is_valid(order, rules):
    for first, second in rules:
        if first not in order or second not in order:
            continue
        
        if order.index(first) > order.index(second):
            return False
    return True

def part1():
    rules = []
    orders = []
    with open("input.txt") as file:
        for line in file.readlines():
            if '|' in line:
                rules.append(tuple(map(int, line.split('|'))))
            if ',' in line:
                orders.append(list(map(int, line.split(','))))
    
    valid_orders = []

    for order in orders:
        if is_valid(order, rules):
            valid_orders.append(order)
    
    sum_of_middles = 0
    for valid_order in valid_orders:
        sum_of_middles += valid_order[len(valid_order)//2]

    return sum_of_middles   

def part2():
    rules = []
    orders = []
    with open("input.txt") as file:
        for line in file.readlines():
            if '|' in line:
                rules.append(tuple(map(int, line.split('|'))))
            if ',' in line:
                orders.append(list(map(int, line.split(','))))
    
    invalid_orders = []

    for order in orders:        
        if not is_valid(order, rules):
            invalid_orders.append(order)

    sum_of_middles = 0
    
    for invalid_order in invalid_orders:
        while not is_valid(invalid_order, rules):
            for first, second in rules:
                if first not in invalid_order or second not in invalid_order:
                    continue

                first_index = invalid_order.index(first)
                second_index = invalid_order.index(second)

                if first_index > second_index:
                    invalid_order[first_index] = second
                    invalid_order[second_index] = first
    
        sum_of_middles += invalid_order[len(invalid_order)//2]

    return sum_of_middles   

if __name__ == "__main__":
    print("Day 5, Part 1: " + str(part1()))
    print("Day 5, Part 2: " + str(part2()))