# Start by opening the input file and splitting the lines to create your grid
with open("testinput.txt", "r") as file:
    lab_map = [list(line.strip()) for line in file]


# Start by defining important information and adding a list of the necessary directions the guard can move
# Find the guard in the grid and make note of its position
# Create a while loop that will impose certain instructions depending on the position of the guard
# If the guard reaches an obstacle "#", position the guard to make a 90 degree right turn and proceed
# The guard leaves an "X" at every position it has been in, when the guard exits the grid, return the sum of "X"s

facing = ["^", ">", "v", "<"]

direction = {                    # (row, column)
    "^" : (-1, 0),               # moving up (up, same)
    ">" : (0, 1),                # moving right (same, right)
    "v" : (1, 0),                # moving down (down, same)
    "<" : (0, -1),               # moving left (same, left)
}

row = len(lab_map)
col = len(lab_map[0])

for i in range(row):
    for j in range(col):
        if lab_map[i][j] in facing:
            guard = (i, j)
            looking = lab_map[i][j]
            break

visited = set([guard])

while True:
    nr, nc = direction[looking]
    new_row, new_col = guard[0] + nr, guard[1] + nc

    if not (0 <= new_row < row and 0 <= new_col < col):
        break

    if lab_map[new_row][new_col] == "#":
        current_index = facing.index(looking)
        looking = facing[(current_index + 1) % 4]
    else:
        guard = (new_row, new_col)
        visited.add(guard)

print(len(visited))


# For Part 2, a new obstruction is introduced: "O"
# This structure is to be strategically placed in order to cause the guard to be stuck in a loop
# The structure cannot be placed at the starting position of the guard
# Objective is to find all possible places the structure can be placed to achieve our goal
# Return the total number of possible placements for the structure


