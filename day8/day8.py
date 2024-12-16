# Open the file as a grid, splitting the lines into rows, the rows into columns

with open("input.txt", "r") as file:
    grid = [list(line.strip()) for line in file]

print(grid)


# I want to make note of every character and position and add them into a dictionary
# I then would like to see if any points are connected by straight lines, this way I can focus on pairs
# Placing antinodes using the initial character as a median to mirror the positions
# Adding the antinodes positions into a set so there are only counted once and returning the sum

character = {}
antinode = set()

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] != ".":
            if grid[i][j] not in character:
                character[grid[i][j]] = set()
            character[grid[i][j]].add((i, j))

print(character)

for char, location in character.items():
    location = list(location)
    for i in range(len(location)):
        for j in range(i + 1, len(location)):
            row1, col1 = location[i]
            row2, col2 = location[j]
            
            endr = row2 - row1
            endc = col2 - col1

            antinode1 = (row1 - endr, col1 - endc)
            antinode2 = (row2 + endr, col2 + endc)

            if 0 <= antinode1[0] < len(grid) and 0 <= antinode1[1] < len(grid[0]):
                antinode.add(antinode1)
            if 0 <= antinode2[0] < len(grid) and 0 <= antinode2[1] < len(grid[0]):
                antinode.add(antinode2)

print(len(antinode))

