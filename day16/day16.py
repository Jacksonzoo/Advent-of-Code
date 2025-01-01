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
    return 0 <= x < len(maze) and 0 <= y < len(maze[0])


def navigate_maze(maze):
    start_x, start_y = find_tile('start', maze)
    
    direction = {
        (-1, 0),        # move up
        (0, 1),         # move left
        (1, 0),         # move down
        (0, -1)         # move right
    }

    queue = [(start_x, start_y)]
    visited = set()
    visited.add((start_x, start_y))
    score = 0

    while queue:
        x, y = queue.pop(0)
        if (x, y) in visited:
            continue

        for dx, dy in direction:
            nx, ny = dx + x, dy + y

            if is_valid(nx, ny, maze) and maze[nx][ny] != '#':
                next_movement = (nx, ny)

                if (nx, ny) == (start_x + 1, start_y):
                    score += 1
                if next_movement not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny))
                
                

                    

                
            








reindeer_maze = open_maze("testinput.txt")

print(reindeer_maze)