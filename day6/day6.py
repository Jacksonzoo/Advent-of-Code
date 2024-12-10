# Start by opening the input file and splitting the lines to create your grid
with open("testinput.txt", "r") as file:
    lab_map = [line.strip() for line in file]

print(lab_map)


# Start by initializing a counter to 0 and adding a list of the necessary directions the guard can move
# Find the guard in the grid and make not of its position
# Create a while loop that will impose certain instructions depending on the position of the guard
# If the guard reaches an obstacle "#", position the guard to make a 90 degree right turn and proceed
# The guard leaves an "X" at every position it has been in, when the guard exits the grid, return the sum of "X"s

x_counter = 0

facing = ["^", ">", "v", "<"]
direction = [       # (row, column)
    (-1,0)          # moving up (up, same)
    (0,1)           # moving right (same, right)
    (1,0)           # moving down (down, same)
    (0,-1)          # moving left (same, left)
]




