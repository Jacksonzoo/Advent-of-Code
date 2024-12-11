# Open and read the input file
with open('input.txt', 'r') as file:
    grid = [list(line.strip()) for line in file]

# Directions: up, right, down, left
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
direction_map = {'^': 0, '>': 1, 'v': 2, '<': 3}

# Locate the guard's starting position and direction
guard_position = None
current_direction = None
for r, row in enumerate(grid):
    for c, cell in enumerate(row):
        if cell in direction_map:
            guard_position = (r, c)
            current_direction = direction_map[cell]
            grid[r][c] = '.'  # Replace the guard's symbol with an empty cell
            break
    if guard_position:
        break

# Set to store visited positions
visited = set()
visited.add(guard_position)

# Grid dimensions
rows = len(grid)
cols = len(grid[0])

# Simulation loop
while True:
    # Calculate next position in the current direction
    dr, dc = directions[current_direction]
    next_r, next_c = guard_position[0] + dr, guard_position[1] + dc

    # Check if the next position is out of bounds
    if next_r < 0 or next_r >= rows or next_c < 0 or next_c >= cols:
        break

    # Check the next cell
    if grid[next_r][next_c] == '#':
        # Turn right (change direction clockwise)
        current_direction = (current_direction + 1) % 4
    else:
        # Move forward
        guard_position = (next_r, next_c)
        visited.add(guard_position)

# Output the result
print(f"Distinct positions visited: {len(visited)}")
