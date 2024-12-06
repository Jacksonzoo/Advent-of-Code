# first open the file with the input and establish a 'results' variable equals to 0

with open("input.txt", "r") as file:
    memory = file.read()

results = 0

# go through each index of the input and see if they follow a pattern. 'mul(x,y)' where x and y are between 1 - 3 digits
n = len(memory)
for i in range(n):
    if memory[i:i+4] == "mul(":
        j = i + 4
        number1 = ""
        for k in range(j, n):
            if memory[k].isdigit():
                number1 += memory[k]
                j += 1
            elif memory[k] == ',':
                break
            else:
                break
        if 1 <= len(number1) <= 3:
            number2 = ""
            for l in range(k + 1, n):
                if memory[l].isdigit():
                    number2 += memory[l]
                    j += 1
                elif memory[l] == ")":
                    j += 1
                    break
                else:
                    break
            if 1 <= len(number2) <= 3 and memory[j] == ")":
                results += int(number1) * int(number2)

# if they do, multiply their x and y values and add them to a 'results' counter
print(results)

# for part 2 we introduce new instructions: "do()"s and "don't()"s
# when we encounter a "do()", this will enable the code to process mul(x,y)
# when we encounter a "don't()", this will disable the code to process mul(x,y) even if it's correctly formatted
with open("input.txt", "r") as file:
    new_memory = file.read()

new_results = 0
enabler = True
n = len(new_memory)

for i in range(n):
    if new_memory[i:i+4] == "do()":
        enabler = True
    elif new_memory[i:i+7] == "don't()":
        enabler = False

    if enabler and new_memory[i:i+4] == "mul(":
        j = i + 4
        number1 = ""
        comma = False
        for k in range(j, n):
            if new_memory[k].isdigit():
                number1 += new_memory[k]
            elif new_memory[k] == ',':
                comma = True
                j = k + 1
                break
            else:
                number1 = ""
                break
        if comma and 1 <= len(number1) <= 3:
            number2 = ""
            paranthesis = False
            for l in range(j, n):
                if new_memory[l].isdigit():
                    number2 += new_memory[l]
                elif new_memory[l] == ")":
                    paranthesis = True
                    break
                else:
                    number2 = ""
                    break
            if 1 <= len(number2) <= 3 and paranthesis:
                if enabler:
                    new_results += int(number1) * int(number2)
print(new_results)
