# Open the input file as a list

def open_stone_line(filename):
    with open(filename, "r") as file:
        stones = file.readline().split()
        arrangement = [int(rock) for rock in stones]
    return arrangement


# Given an arrangement of stones, each with an engraved number. 
# After every blink of your eyes, certain rules are applied to each stone depending on the number engraved on it
# If the number engraved is 0, repalce it with a stone with the number 1 engraved
# If the stone has a number whose digits are an even number, the digits are cut in half and the stone is split
# maintaing its order, the left stone engraves the left half of the digits and the right stone contains the other
# for example: the number 1234 is engraved. The stone is split where the 12 is engraved to the left stone and 34 engraved on the right
# If none of the rules is applicable to the number engraved, multiply that number by 2024
# After 25 blinks, how many stones do we have in this arrangement

def split_digit(stone_number):
    stone_str = str(stone_number)
    middle = len(stone_str) // 2

    left_half = int(stone_str[:middle])
    right_half = int(stone_str[middle:])

    return left_half, right_half

def apply_rule(arrangement):
    new_arrangement = []
    for stone in arrangement:
        if stone == 0:
            new_arrangement.append(1)
        elif len(str(stone)) % 2 == 0:
            left_stone, right_stone = split_digit(stone)
            new_arrangement.extend([left_stone, right_stone])
        else:
            new_arrangement.append(stone * 2024)
    return new_arrangement

def blinking_25_times(arrangement):
    blink = 0
    while blink < 25:
        arrangement = apply_rule(arrangement)
        blink += 1
    return arrangement

def total_stones(arrangement):
    total = len(blinking_25_times(arrangement))
    return total


stone_arrangement = open_stone_line("input.txt")

print(total_stones(stone_arrangement))


# For part 2, find how many stones would we have after blinking 75 times

def blinking_75_times(arrangement):
    stone_count = {}

    for stone in arrangement:
        if stone in stone_count:
            stone_count[stone] += 1
        else:
            stone_count[stone] = 1

    for _ in range(75):
        new_count = {}
        for stone, count in stone_count.items():
            if stone == 0:
                new_count[1] = new_count.get(1, 0) + count
            elif (len(str(stone)) % 2 == 0):
                left, right = split_digit(stone)
                new_count[left] = new_count.get(left, 0) + count
                new_count[right] = new_count.get(right, 0) + count
            else:
                multiplied_stone = stone * 2024
                new_count[multiplied_stone] = new_count.get(multiplied_stone, 0) + count
        stone_count = new_count
    return sum(stone_count.values())
    
def total_stone_75(arrangement):
    return blinking_75_times(arrangement)

print(total_stone_75(stone_arrangement))

