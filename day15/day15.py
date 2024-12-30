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

def open_bigger_map(filename):
    with open(filename, "r") as file:
        content = file.read()
        section_one, section_two = content.split('\n\n')
        warehouse_map = [list(line) for line in section_one.split()]
        move_instruction = list("".join(section_two.split()))

        bigger_warehouse = []

        for i in range(len(warehouse_map)):
            bigger_warehouse_row = []
            for j in range(len(warehouse_map[0])):
                current_value = warehouse_map[i][j]
                if current_value == '#':
                    bigger_warehouse_row.append('#')
                    bigger_warehouse_row.append('#')
                elif current_value == '.':
                    bigger_warehouse_row.append('.')
                    bigger_warehouse_row.append('.')
                elif current_value == 'O':
                    bigger_warehouse_row.append('[')
                    bigger_warehouse_row.append(']')
                elif current_value == '@':
                    bigger_warehouse_row.append('@')
                    bigger_warehouse_row.append('.')

            bigger_warehouse.append(bigger_warehouse_row)

    return bigger_warehouse, move_instruction


def is_box(value):
    return value in ['[',']']

def get_box_width():
    return 2

def is_box_start(char):
    return char == '['

def is_empty(value):
    return value == '.'

def new_box_positions(bigger_warehouse, visited_positions, dx, dy):
    for x, y in reversed(visited_positions):
        nx, ny = x + dx, y + dy
        bigger_warehouse[nx][ny] = bigger_warehouse[x][y]
        bigger_warehouse[x][y] = '.'

def locate_box_group(warehouse_map, robot_x, robot_y, dx, dy):
    if warehouse_map[robot_x][robot_y] not in ['#', '.']:
        group = [(robot_x, robot_y)]
        warehouse_map[robot_x][robot_y] = '.'
        
        if within_warehouse(robot_x + dx, robot_y + dy, warehouse_map):
            group.extend(locate_box_group(warehouse_map, robot_x + dx, robot_y + dy, dx, dy))
        
        if within_warehouse(robot_x, robot_y + 1, warehouse_map) and warehouse_map[robot_x][robot_y + 1] == ']':
            group.extend(locate_box_group(warehouse_map, robot_x, robot_y + 1, dx, dy))
        
        if within_warehouse(robot_x, robot_y - 1, warehouse_map) and warehouse_map[robot_x][robot_y - 1] == '[':
            group.extend(locate_box_group(warehouse_map, robot_x, robot_y - 1, dx, dy))
            
        return group
    return []

def move_robot_new(warehouse_map, move_instruction):
    robot_x, robot_y = locate_robot(warehouse_map)
    directions = movement()

    for move in move_instruction:
        dx, dy = directions[move]
        boxes = locate_box_group(warehouse_map.copy(), robot_x, robot_y, dx, dy)
        
        if boxes and all(within_warehouse(x + dx, y + dy, warehouse_map) and 
                        warehouse_map[x + dx][y + dy] == '.' for x, y in boxes):
            for x, y in boxes:
                warehouse_map[x + dx][y + dy] = warehouse_map[x][y]
                warehouse_map[x][y] = '.'
            robot_x += dx
            robot_y += dy

    return warehouse_map



def move_robot_working(bigger_warehouse, move_instruction):
    robot_x, robot_y = locate_robot(bigger_warehouse)
    directions = movement()

    for move in move_instruction:
        dx, dy = directions[move]
        nx, ny = robot_x + dx, robot_y  + dy

        if not within_warehouse(nx, ny, bigger_warehouse):
            continue

        next_movement = bigger_warehouse[nx][ny]

        if next_movement == '.':
            bigger_warehouse[robot_x][robot_y] = "."
            bigger_warehouse[nx][ny] = '@'
            robot_x, robot_y = nx, ny
        elif is_box(next_movement):
            visited = []
            current_x, current_y = nx, ny

            while within_warehouse(current_x, current_y, bigger_warehouse) and is_box(bigger_warehouse[current_x][current_y]):
                visited.append((current_x, current_y))
                current_x += dx
                current_y += dy

            if within_warehouse(current_x, current_y, bigger_warehouse) and is_empty(bigger_warehouse[current_x][current_y]):
                for pos_x, pos_y in reversed(visited):
                    next_x, next_y = pos_x + dx, pos_y + dy
                    bigger_warehouse[next_x][next_y] = bigger_warehouse[pos_x][pos_y]
                    bigger_warehouse[pos_x][pos_y] = '.'
                bigger_warehouse[nx][ny] = '@'
                bigger_warehouse[robot_x][robot_y] = '.'
                robot_x, robot_y = nx, ny

    return bigger_warehouse


def robot_part2_draft(bigger_warehouse, move_instruction):
    robot_x, robot_y = locate_robot(bigger_warehouse)
    directions = movement()

    for move in move_instruction:
        dx, dy = directions[move]
        nx, ny = robot_x + dx, robot_y  + dy

        if not within_warehouse(nx, ny, bigger_warehouse):
            continue

        next_movement = bigger_warehouse[nx][ny]

        if next_movement == '.':
            bigger_warehouse[robot_x][robot_y] = "."
            bigger_warehouse[nx][ny] = '@'
            robot_x, robot_y = nx, ny
            if move == '<' or '>':
                look_ahead_x, look_ahead_y = nx + dx + dx, ny + dy + dy
            else:
                look_ahead_x, look_ahead_y = nx + dx, ny + dy
            while within_warehouse(look_ahead_x, look_ahead_y, bigger_warehouse) and bigger_warehouse[look_ahead_x][look_ahead_y] == '[' or ']':
                if move == '<' or '>':
                    look_ahead_x += dx + dx
                    look_ahead_y += dy + dy
                else:
                    look_ahead_x += dx
                    look_ahead_y += dy
            if within_warehouse(look_ahead_x, look_ahead_y, bigger_warehouse):
                if bigger_warehouse[look_ahead_x][look_ahead_y] == '.':
                    bigger_warehouse[robot_x][robot_y] = '.'
                    bigger_warehouse[nx][ny] = '@'
                    if move == '<' or '>':
                        for x in (nx, look_ahead_x + 1):
                            for y in (ny, look_ahead_y + 1):
                                bigger_warehouse[x][y] = '[' if (x + y) % 2 == 0 else ']'
                    else:
                        visited = set()
                        visited.add(nx, ny)
                        for temp_x, temp_y in directions:
                            new_x, new_y = temp_x + nx, temp_y + ny
                            while set:
                                if bigger_warehouse[new_x][new_y] == '[' or ']':
                                    visited.add(new_x, new_y)
                                else:
                                    break
                        for position in reversed(visited):
                            pos_x, pos_y = position
                            next_pox, next_poy = pos_x + dx, pos_y + dy
                            bigger_warehouse[next_pox][next_poy] = bigger_warehouse[pos_x][pos_y]
                            if bigger_warehouse[pos_x][pos_y] != '[' or ']':
                                bigger_warehouse[pos_x][pos_y] = '.'

                    robot_x, robot_y = nx, ny

    return bigger_warehouse


def calc_new_gps_sum(bigger_warehouse):
    gps_sum = 0
    for i in range(len(bigger_warehouse)):
        for j in range(len(bigger_warehouse[0])-1):
            if bigger_warehouse[i][j] == '[' and bigger_warehouse[i][j+1] == ']':
                gps_coordinate = 100 * i + j
                gps_sum += gps_coordinate
                
    return gps_sum


bigger_warehouse, move_direction = open_bigger_map("testinput.txt")
new_robot_movement = move_robot_new(bigger_warehouse, move_instruction)
gps_sum = calc_new_gps_sum(new_robot_movement)


print(gps_sum)



# Part (unfinished):

def extract_component(map, r, c, dr, dc):
    """
    Recursively extract connected components of the map (e.g., wide boxes, robot).
    """
    if map[r][c] in ['#', '.']:
        return []
    ch = map[r][c]
    map[r][c] = '.'  # Mark as visited
    component = [(r, c, ch)]
    component.extend(extract_component(map, r + dr, c + dc, dr, dc))
    if ch == '[':
        component.extend(extract_component(map, r, c + 1, dr, dc))
    if ch == ']':
        component.extend(extract_component(map, r, c - 1, dr, dc))
    return component

def solve(map, moves):
    """
    Simulate the robot's movements and calculate the GPS sum of all boxes.
    """
    robot_r, robot_c = next((r, row.index('@')) for r, row in enumerate(map) if '@' in row)
    for move in moves:
        dr, dc = {'v': (1, 0), '^': (-1, 0), '>': (0, 1), '<': (0, -1)}[move]
        component = extract_component(map, robot_r, robot_c, dr, dc)
        if all(map[r + dr][c + dc] == '.' for r, c, _ in component):
            component = [(r + dr, c + dc, ch) for r, c, ch in component]
            robot_r, robot_c = robot_r + dr, robot_c + dc
        for rr, cc, ch in component:
            map[rr][cc] = ch
    return sum(r * 100 + c for r, row in enumerate(map) for c, ch in enumerate(row) if ch in ['O', '['])

def double(ch):
    """
    Scale characters for Part 2.
    """
    if ch == '@':
        return ['@', '.']
    elif ch == '.':
        return ['.', '.']
    elif ch == '#':
        return ['#', '#']
    elif ch == 'O':
        return ['[', ']']
    else:
        raise Exception("Unexpected char " + ch)

# ---------------- MAIN DRIVER ------------------
if __name__ == "__main__":
    # Replace 'testinput.txt' with the actual file path
    with open("testinput.txt", "r") as file:
        content = file.read()
        map_data, move_data = content.split("\n\n")

    map1 = [list(row) for row in map_data.split('\n')]
    moves = list(move_data.replace('\n', ''))

    # Part 2: Scale the map and solve
    map2 = [sum((double(ch) for ch in row), []) for row in map_data.split('\n')]

    part2_gps_sum = solve(map2, moves)
    print(f"Part Unfinished GPS Sum: {part2_gps_sum}")
