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

def movement(move_instruction):
    return {
        '^': (-1, 0),
        '>': (0, 1),
        'v': (1, 0),
        '<': (-1, 0)
    }

def locate_robot(warehouse_map):
    for i in range(len(warehouse_map)):
        for j in range(len(warehouse_map[0])):
            if warehouse_map[i][j] != '@':
                continue
            else:
                robot = (i, j)
    return robot

def next_position(nx, ny, warehouse_map):
    for i in range(len(warehouse_map)):
        for j in range(len(warehouse_map[0])):
            return warehouse_map[nx][ny]


def move_robot(warehouse_map, move_instruction):
    robot = locate_robot(warehouse_map)
    row = len(warehouse_map)
    col = len(warehouse_map[0])
    directions = movement(move_instruction)

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
                                end_x, end_y = sequence[-1]
                                warehouse_map[new_start_x][new_start_y] = warehouse_map[original_x][original_y]
                                warehouse_map[original_x][original_y] = '.'
                                warehouse_map[end_x][end_y] = 'O'
    finished_map = warehouse_map
    return finished_map

def calculate_gps_sum(finished_map):
    gps_coordinate_sum = 0
    for i in range(len(finished_map)):
        for j in range(len(finished_map[0])):
            if finished_map != 'O':
                continue
            else:
                height_distance = abs(0 - i)
                left_distance = abs(0 - j)
                gps_coordinate = 100 * (height_distance + left_distance)
                gps_coordinate_sum += gps_coordinate

    return gps_coordinate_sum



warehouse_map, move_instruction = open_map_instructions("testinput.txt")
robot_movement = move_robot(warehouse_map, move_instruction)
gps_sum = calculate_gps_sum(robot_movement)

print(gps_sum)

