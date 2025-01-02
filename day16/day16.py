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
        (-1, 0),  # up (north)
        (0, 1),   # right (east)
        (1, 0),   # down (south)
        (0, -1)   # left (west)
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


# Part 2 we need to find how many non-wall tiles (S, ., E) are one of the 'best' paths to take. 
# How many tiles are in at least one of the best possible paths to take

def find_best_tiles(maze, start, end):
    directions = [
        (-1, 0),  # up (north)
        (0, 1),   # right (east)
        (1, 0),   # down (south)
        (0, -1)   # left (west)
    ]
    
    queue = [(0, start[0], start[1], 1)] 
    forward_scores = {} 
    
    while queue:
        queue.sort()
        score, x, y, current_dir = queue.pop(0)
        
        state = (x, y, current_dir)
        if state in forward_scores and forward_scores[state] <= score:
            continue
        forward_scores[state] = score
        
        for i, (dx, dy) in enumerate(directions):
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny, maze):
                new_score = score + (1 if i == current_dir else 1001)
                queue.append((new_score, nx, ny, i))
    
    optimal_score = float('inf')
    end_directions = []
    for dir_idx in range(4):
        state = (end[0], end[1], dir_idx)
        if state in forward_scores:
            if forward_scores[state] < optimal_score:
                optimal_score = forward_scores[state]
                end_directions = [dir_idx]
            elif forward_scores[state] == optimal_score:
                end_directions.append(dir_idx)
    
    best_tiles = {start, end} 
    queue = [(optimal_score, end[0], end[1], d) for d in end_directions]
    backward_visited = set()
    
    while queue:
        queue.sort(reverse=True)
        target_score, x, y, current_dir = queue.pop()
        
        state = (x, y, current_dir)
        if state in backward_visited:
            continue
        backward_visited.add(state)
        
        for prev_dir, (dx, dy) in enumerate(directions):
            px, py = x - dx, y - dy
            if is_valid(px, py, maze):
                move_cost = 1 if prev_dir == current_dir else 1001
                prev_score = target_score - move_cost
                prev_state = (px, py, prev_dir)
                
                if prev_state in forward_scores and forward_scores[prev_state] == prev_score:
                    best_tiles.add((px, py))
                    queue.append((prev_score, px, py, prev_dir))
    
    return best_tiles

def count_best_tiles(maze):
    start = find_tile('start', maze)
    end = find_tile('end', maze)
    best_tiles = find_best_tiles(maze, start, end)
    
    return len(best_tiles)

reindeer_maze_part2 = open_maze("testinput.txt")
tile_count = count_best_tiles(reindeer_maze)
print(tile_count)

