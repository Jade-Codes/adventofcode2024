
def is_all_increasing(first_number, second_number, third_number):
    return first_number < second_number < third_number

def is_all_decreasing(first_number, second_number, third_number):
    return first_number > second_number > third_number

def is_in_range(first_number, second_number):
    return 1 <= abs(first_number-second_number) <= 3

def part1():
    reports = []

    with open("input.txt") as file:
        reports = file.readlines()

    is_not_safe = 0

    for report in reports:
        numbers = list(map(int, report.split(' ')))

        for i in range(len(numbers)-1):
            if is_in_range(numbers[i], numbers[i+1]) is False:
                is_not_safe += 1
                break

            if i == 0:
                continue

            if is_all_increasing(numbers[i-1], numbers[i], numbers[i+1]) is False and \
                is_all_decreasing(numbers[i-1], numbers[i], numbers[i+1]) is False:
                is_not_safe += 1
                break
    
    safe_reports = len(reports) - is_not_safe
    return  safe_reports

def part2():
    reports = []

    with open("input.txt") as file:
        reports = file.readlines()

    not_safe_counter = 0

    for report in reports:
        numbers = list(map(int, report.split(' ')))

        is_not_safe = False

        for i in range(len(numbers)-2):
            if is_in_range(numbers[i], numbers[i+1]) is False:
                if is_in_range(numbers[i], numbers[i+2]) is False:
                    is_not_safe = True
                    break

            if i == 0:
                continue

            if is_all_increasing(numbers[i-1], numbers[i], numbers[i+1]) is False and \
                is_all_decreasing(numbers[i-1], numbers[i], numbers[i+1]) is False and \
                is_all_increasing(numbers[i-1], numbers[i+1], numbers[i+2]) is False and \
                is_all_decreasing(numbers[i-1], numbers[i+1], numbers[i+2]) is False:
                    is_not_safe = True
                    break

        for i in range(len(numbers)-2):
            numbers.reverse()
            if is_in_range(numbers[i], numbers[i+1]) is False:
                if is_in_range(numbers[i], numbers[i+2]) is False:
                    is_not_safe = True
                    break

            if i == 0:
                continue

            if is_all_increasing(numbers[i-1], numbers[i], numbers[i+1]) is False and \
                is_all_decreasing(numbers[i-1], numbers[i], numbers[i+1]) is False and \
                is_all_increasing(numbers[i-1], numbers[i+1], numbers[i+2]) is False and \
                is_all_decreasing(numbers[i-1], numbers[i+1], numbers[i+2]) is False:
                    is_not_safe = True
                    break
            
        if is_not_safe:
            not_safe_counter += 1

    safe_reports = len(reports) - not_safe_counter
    return  safe_reports


if __name__ == "__main__":
    print("Day 2, Part 1: " + str(part1()))
    print("Day 2, Part 2: " + str(part2()))