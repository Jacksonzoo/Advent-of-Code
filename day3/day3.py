# first open the file with the input and establish a 'results' variable equals to 0

with open("input.txt", "r") as file:
    memory = file.read()
print(memory)

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

# if they do, multiply their x and y values and add them to a 'results' counter.
print(results)

