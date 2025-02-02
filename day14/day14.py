# Open the input files as usable instrucitons

def open_instructions(filename):
    robot_pv = []
    testing = filename == "testinput.txt"

    with open(filename, "r") as file:
        lines = [line.split() for line in file]
        for line in lines:
            px = int(line[0].split('=')[1].split(',')[0])
            py = int(line[0].split('=')[1].split(',')[1])
            vx = int(line[1].split('=')[1].split(',')[0])
            vy = int(line[1].split('=')[1].split(',')[1])

            robot_pv.append({
                'p': (px, py),
                'v': (vx, vy)
            })

    return robot_pv, testing


# Part 1, given a list of instructions of robot positions (p) and how they move along a tile each second (v),
# the goal is to find a safety score which is obtained by dividing the grid into 4 equal quadrants and
# multiplying how many robots are in each quadrant by each other
# Note that if robots move 'outside' the grid, they essentially move to the other side as if it were an extended grid
# Robots can also overlap with each other

def choose_grid(testing):
    return (11, 7) if testing else (101, 103)


def robot_movement(robot, grid_size):
    width, height = grid_size
    final_positions = {}

    for robo in robot:
        px, py = robo['p']
        vx, vy = robo['v']

        for i in range(100):
            px = (px + vx) % width
            py = (py + vy) % height

        final_positions[(px, py)] = final_positions.get((px, py), 0) + 1

    return final_positions


def calculate_safety_score(final_positions, grid_size):
    width, height =  grid_size
    mid_x, mid_y = width // 2, height // 2

    quadrant_count = [0, 0, 0, 0]

    for (px, py), count in final_positions.items():
        if px == mid_x or py == mid_y:
            continue
        elif px < mid_x and py < mid_y:
            quadrant_count[0] += count
        elif px > mid_x and py < mid_y:
            quadrant_count[1] += count
        elif px < mid_x and py > mid_y:
            quadrant_count[2] += count
        elif px > mid_x and py > mid_y:
            quadrant_count[3] += count

    safety_score = 1
    for count in quadrant_count:
        safety_score *= count

    return safety_score


robot_rules, testing = open_instructions("input.txt")
grid_size = choose_grid(testing)
final_position = robot_movement(robot_rules, grid_size)
safety_score = calculate_safety_score(final_position, grid_size)

print(safety_score)


# Part 2 apparently the robots arrange themselves to look like a christmas tree 
# after a certain amount of seconds. The goal is to find how many seconds that is
# Assuming that for a grid this big you would need all the robots to form a decent tree
# Each robot should not be overlapping

def robot_movement(robot, grid_size, seconds):
    width, height = grid_size
    final_position = {}

    for robots in robot:
        px, py = robots['p']
        vx, vy = robots['v']

        nx = (px + vx * seconds) % width
        ny = (py + vy * seconds) % height
        final_position[(nx, ny)] = final_position.get((nx, ny), 0) + 1
    
    return final_position

def check_overlap(robot, grid_size):
    seconds = 0

    while True:
        seconds += 1
        final_position = robot_movement(robot, grid_size, seconds)

        if all(count == 1 for count in final_position.values()):
            return seconds, final_position
        

robot_part_two, testing = open_instructions("input.txt")
grid_size_two = choose_grid(testing)
seconds, final_position = check_overlap(robot_part_two, grid_size_two)

print(seconds)