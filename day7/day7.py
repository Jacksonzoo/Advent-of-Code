# Open the input file and store it in a dictionary by test value and operations numbers
with open("input.txt", "r") as file:
    equation = {}
    for line in file:
        part = line.split(":")
        test = int(part[0])
        operation = list(map(int, part[1].split()))
        equation[test] = operation
print(equation)

# Goal is to find and ultimately sum up the test numbers where the (multiplicaiton or addition) between
# the operational numbers from left to right can equate the test value.
# I would like to use a recursive statement explore operator combinations to find possible solutions.


valid = set()


for test, operation in equation.items():
    stack = [(operation[0], 0)]

    while stack:
        current_value, index = stack.pop()

        if current_value > test:
            continue
        if index == len(operation) - 1:
            if current_value == test:
                valid.add(test)
            continue

        next_operation = operation[index + 1]

        stack.append((current_value + next_operation, index + 1))
        stack.append((current_value * next_operation, index + 1))

test_sum = sum(valid)
print(test_sum)


# Part 2 introduces a new operator (||), this operator essentially concatenates 2 numbers together (2 || 3 = 23)
# Include this operator along with multiplication and addition to see if we have a new sum

valid_two = set()

for test, operation in equation.items():
    stack = [(operation[0], 0)]

    while stack:
        current_value, index = stack.pop()

        if current_value > test:
            continue
        if index == len(operation) - 1:
            if current_value == test:
                valid_two.add(test)
            continue

        next_operation = operation[index + 1]

        stack.append((current_value + next_operation, index + 1))
        stack.append((current_value * next_operation, index + 1))
        stack.append((int(str(current_value) + str(next_operation)), index + 1))


second_test = sum(valid_two)
print(second_test)

