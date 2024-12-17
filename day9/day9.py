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


# For part 2, we would like to compact the disk in a way where we do not have so many free space
# We will now be moving the files in groups of ID into the availiable free space as opposed to one by one

block_two = []
checksum_two = 0

file_id = 0
for i in range(len(disk)):
    if i % 2 == 0:
        for j in range(int(disk[i])):
            block_two.append(file_id)
        file_id += 1
    else:
        for j in range(int(disk[i])):
            block_two.append(".")

for file_id in sorted(set(x for x in block_two if x != "."), reverse=True):
    file_location = [idx for idx, val in enumerate(block_two) if val == file_id]
    if not file_location:
        continue

    file_start = min(file_location)
    file_size = len(file_location)

    free_space = []
    free = None

    for i in range(len(block_two)):
        if block_two[i] == ".":
            if free is None:
                free = i
        else:
            if free is not None:
                length = i - free
                free_space.append((free, length))
                free = None

    if free is not None:
        length = len(block_two) - free
        free_space.append((free, length))


    moved = False
    for free, length in free_space:
        if length >= file_size and (free + file_size) <= file_start:
            for location in file_location:
                block_two[location] = "."

            for j in range(file_size):
                block_two[free + j] = file_id

            moved = True
            break

for index in range(len(block_two)):
    if block_two[index] != ".":
        value = block_two[index] * index
        checksum_two += value


print(checksum_two)