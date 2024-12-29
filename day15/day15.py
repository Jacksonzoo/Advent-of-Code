# Open the file returning a map and a list of directional instructions

def open_map_instructions(filename):
    with open(filename, "r") as file:
        content = file.read()
        section_one, section_two = content.split('\n\n')
        warehouse_map = [list(line) for line in section_one.split()]
        move_instruction = list("".join(section_two.split()))

    return warehouse_map, move_instruction


# Part 1, tasked to find the total sum of all boxes gps coordinates (100 * distance from top edge + left edge of map)
# Robot (@) can push boxes (O) as long as the other side is not a wall (#)
# After the robot moves in order of the sequence in directional instructions, calculate the sum of all box gps coordinate locations

def movement():
    return {
        '^': (-1, 0),
        '>': (0, 1),
        'v': (1, 0),
        '<': (0, -1)
    }

def locate_robot(warehouse_map):
    for i in range(len(warehouse_map)):
        for j in range(len(warehouse_map[0])):
            if warehouse_map[i][j] == '@':
                return (i, j)

def within_warehouse(nx, ny, warehouse_map):
    return 0 <= nx < len(warehouse_map) and 0 <= ny < len(warehouse_map[0])

def move_robot_draft(warehouse_map, move_instruction):
    robot = locate_robot(warehouse_map)
    row = len(warehouse_map)
    col = len(warehouse_map[0])
    directions = movement(move_instruction)

    def next_position(nx, ny, warehouse_map):
            return warehouse_map[nx][ny]
    
    for i in range(row):
        for j in range(col):
            if (i, j) == robot:
                x, y = i, j
                for move in move_instruction:
                    for arrow, value in directions.items():
                        if move == arrow:
                            dx, dy = value
                            nx, ny = x + dx, y + dy
                            if next_position(nx, ny, warehouse_map) == 'O':
                                look_ahead_x, look_ahead_y = nx + dx, nx + dy
                                sequence = [(nx, ny)]
                                while sequence:
                                    look_ahead_x, look_ahead_y = look_ahead_x + dx, look_ahead_y + dy
                                    if warehouse_map[look_ahead_x][look_ahead_y] == 'O':
                                        sequence.append((look_ahead_x, look_ahead_y))
                                    elif warehouse_map[look_ahead_x][look_ahead_y] == ".":
                                        sequence.append(look_ahead_x, look_ahead_y)
                                        break
                                    elif warehouse_map[look_ahead_x][look_ahead_y] == '#':
                                        break
                                original_x, original_y = sequence[0]
                                new_start_x, new_start_y = sequence[1]
                                if len(sequence) > 2:
                                    end_x, end_y = sequence[-1]
                                    warehouse_map[end_x][end_y] = 'O'
                                warehouse_map[new_start_x][new_start_y] = warehouse_map[original_x][original_y]
                                warehouse_map[original_x][original_y] = '.'
    finished_map = warehouse_map
    return finished_map

def move_robot(warehouse_map, move_instruction):
    robot_x, robot_y = locate_robot(warehouse_map)
    directions = movement()

    for move in move_instruction:
        dx, dy = directions[move]
        nx, ny = robot_x + dx, robot_y  + dy

        if not within_warehouse(nx, ny, warehouse_map):
            continue

        next_movement = warehouse_map[nx][ny]

        if next_movement == '.':
            warehouse_map[robot_x][robot_y] = "."
            warehouse_map[nx][ny] = '@'
            robot_x, robot_y = nx, ny
        elif warehouse_map[nx][ny] == 'O':
            look_ahead_x, look_ahead_y = nx + dx, ny + dy
            while within_warehouse(look_ahead_x, look_ahead_y, warehouse_map) and warehouse_map[look_ahead_x][look_ahead_y] == 'O':
                look_ahead_x += dx
                look_ahead_y += dy
            if within_warehouse(look_ahead_x, look_ahead_y, warehouse_map):
                if warehouse_map[look_ahead_x][look_ahead_y] == '.':
                    warehouse_map[look_ahead_x][look_ahead_y] = 'O'
                    warehouse_map[nx][ny] = '@'
                    warehouse_map[robot_x][robot_y] = '.'
                    robot_x, robot_y = nx, ny

    return warehouse_map

def calculate_gps_sum(warehouse_map):
    gps_coordinate_sum = 0
    for i in range(len(warehouse_map)):
        for j in range(len(warehouse_map[0])):
            if warehouse_map[i][j] == 'O':
                gps_coordinate_sum += 100 * i + j

    return gps_coordinate_sum

warehouse_map, move_instruction = open_map_instructions("input.txt")
robot_movement = move_robot(warehouse_map, move_instruction)
gps_sum = calculate_gps_sum(robot_movement)

print(gps_sum)


# Part 2 the warehouse map has doubled
# For every '#', there is a '##'; for every 'O' there is a '[]'; for every '.' there is '..'; for every '@' there is '@.'
# Now the goal is to find new gps sum for each box position using the ']' edge when calculating distance from left wall.
# If box(a) is pushing in between ('c][d') box(c) and box(d) robot a can push box(a) moving box(c) and box(d) along with it.
# Say if we got a 4 stack pyramid where robot was pushing box 1a. if box 4d were to hit a wall, the entire structure stops.

