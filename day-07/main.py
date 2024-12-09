def part1():
    equations = []

    with open("input.txt") as file:
        equations = file.readlines()

    calibration_result = 0

    for equation in equations:
        test_value = int(equation.split(':')[0])
        numbers = [int(x.strip('\n')) for x in (equation.split(':')[1]).split(' ') if x.strip('\n').isdigit()]

        dp = {}
        dp[0] = set([numbers[0]])
        
        for i in range(1, len(numbers)):
            number = numbers[i]
            dp[i] = set([])
            for previous_number in dp[i-1]:
                if previous_number + number <= test_value:
                    dp[i].add(previous_number + number)
                if previous_number * number <= test_value:
                    dp[i].add(previous_number * number)
        
        if test_value in dp[len(numbers)-1]:
            calibration_result += test_value
    
    return calibration_result

def part2():
    equations = []

    with open("input.txt") as file:
        equations = file.readlines()

    calibration_result = 0

    for equation in equations:
        test_value = int(equation.split(':')[0])
        numbers = [int(x.strip('\n')) for x in (equation.split(':')[1]).split(' ') if x.strip('\n').isdigit()]

        dp = {}
        dp[0] = set([numbers[0]])
        
        for i in range(1, len(numbers)):
            number = numbers[i]
            dp[i] = set([])
            for previous_number in dp[i-1]:
                if previous_number + number <= test_value:
                    dp[i].add(previous_number + number)
                if previous_number * number <= test_value:
                    dp[i].add(previous_number * number)
                if int(str(previous_number)+str(number)) <= test_value:
                    dp[i].add(int(str(previous_number)+str(number)))
        
        if test_value in dp[len(numbers)-1]:
            calibration_result += test_value
    
    return calibration_result

if __name__ == "__main__":
    print("Day 7, Part 1: " + str(part1()))
    print("Day 7, Part 2: " + str(part2()))