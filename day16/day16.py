# Open the reindeer maze as a 2 D grid
def open_maze(filename):
    with open (filename, "r") as file:
        maze = [list(line.strip()) for line in file]

    return maze


# Part 1 the task is to naviage the maze from S (start), facing east, to end at E (end).
# For each possible move forward (cannot move into wall #) your score increases by 1 point.
# For each 90 degree turn (clockwise or counterclockwise) your score increases by 1000 points.
# Find a way to complete the maze producing the lowest score

def find_tile(tile, maze):
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if tile == 'start' and maze[i][j] == 'S':
                return (i, j)
            elif tile == 'end' and maze[i][j] == 'E':
                return (i, j)
            

def is_valid(x, y, maze):
    return 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] != '#'


def navigate_maze(maze, start, end):
    direction = [
        (-1, 0),        # move up
        (0, 1),         # move left
        (1, 0),         # move down
        (0, -1)         # move right
    ]

    queue = [(0, start[0], start[1], 1)]
    visited = set()

    while queue:
        queue.sort()
        score, x, y, current_dir = queue.pop(0)
        if (x, y) == end:
            return score
        if (x, y, current_dir) in visited:
            continue
        visited.add((x, y, current_dir))

        for i, (dx, dy) in enumerate(direction):
            nx, ny = dx + x, dy + y

            if is_valid(nx, ny, maze):
                if i == current_dir:
                    new_score = score + 1
                else:
                    new_score = score + 1000 + 1
                
                queue.append((new_score, nx, ny, i))

    return float('inf')

def find_lowest_score(maze):
    start = find_tile('start', maze)
    end = find_tile('end', maze)

    return navigate_maze(maze, start, end)



reindeer_maze = open_maze("input.txt")
lowest_score = find_lowest_score(reindeer_maze)

print(lowest_score)




