# Open the file into a simple array

with open("input.txt", "r") as files:
    disk = files.read()


# I want to parse through each number and assign it an "ID" value i < len array i ++
# Next divide each number by alternating between them as file then free space
# Create a new array to store the number of block files for each ID and "." number of free spaces
# Then move file blocks one at a time from the end of the array to the first free space in the array
# Each file block position would then need to be multiplied by the ID of the file; incremented in a counter
# Return the sum

checksum = 0
block = []
file_id = 0

for i in range(len(disk)):
    if i % 2 == 0:
        for j in range(int(disk[i])):
            block.append(file_id)
        file_id += 1
    else:
        for j in range(int(disk[i])):
            block.append(".")


while True:
    free_index = None

    for index in range(len(block)):
        if block[index] == ".":
            if any(value != "." for value in block[index + 1:]):
                free_index = index
                break

    if free_index is None:
        break

    last_file = None
    for index in range(len(block) -1, -1, -1):
        if block[index] != ".":
            last_file = index
            break

    file_block = block.pop(last_file)
    block[free_index] = file_block

for index in range(len(block)):
    if block[index] != ".":
        value = block[index] * index
        checksum += value

print(checksum)