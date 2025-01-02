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

from heapq import heappop, heappush


def is_valid(x, y, maze):
    """
    Check if the position (x, y) is within the maze and not a wall (#).
    """
    return 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] != '#'


def find_tile(tile, maze):
    """
    Find the position of the given tile ('start' or 'end') in the maze.
    """
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if tile == 'start' and maze[i][j] == 'S':
                return (i, j)
            elif tile == 'end' and maze[i][j] == 'E':
                return (i, j)


def dijkstra_with_backtracking(maze, start, end):
    """
    Implements Dijkstra's algorithm with backtracking to find the lowest-cost paths.
    Tracks all valid transitions to reconstruct paths later.
    """
    directions = [
        (-1, 0),  # up (north)
        (0, 1),   # right (east)
        (1, 0),   # down (south)
        (0, -1)   # left (west)
    ]

    queue = [(0, start[0], start[1], 1)]  # (cost, x, y, direction)
    visited = {}
    came_from = {}

    best_score = float('inf')

    while queue:
        cost, x, y, current_dir = heappop(queue)

        # Stop processing if we exceed the best score found
        if cost > best_score:
            continue

        # Skip if we've already visited this state with a better or equal score
        if (x, y, current_dir) in visited and visited[(x, y, current_dir)] <= cost:
            continue

        visited[(x, y, current_dir)] = cost

        # Track predecessors for backtracking
        if (x, y, current_dir) not in came_from:
            came_from[(x, y, current_dir)] = set()

        # If we reach the end, update the best score
        if (x, y) == end:
            if cost < best_score:
                best_score = cost
            continue

        # Explore neighbors
        for i, (dx, dy) in enumerate(directions):
            nx, ny = x + dx, y + dy

            if is_valid(nx, ny, maze):
                new_cost = cost + 1 if i == current_dir else cost + 1001
                new_state = (nx, ny, i)

                if new_state not in came_from:
                    came_from[new_state] = set()

                came_from[new_state].add((x, y, current_dir))
                heappush(queue, (new_cost, nx, ny, i))

    return best_score, came_from


def iterative_backtrack_paths(came_from, end_state):
    """
    Iteratively backtrack to find all unique tiles in paths from the end_state to start.
    """
    all_paths_tiles = set()
    stack = [(end_state, [(end_state[0], end_state[1])])]  # (current_state, path)

    while stack:
        current_state, path = stack.pop()
        all_paths_tiles.update(path)

        for prev_state in came_from.get(current_state, []):
            if prev_state not in path:
                stack.append((prev_state, path + [(prev_state[0], prev_state[1])]))

    return all_paths_tiles


def count_unique_best_path_tiles_iterative(maze):
    """
    Counts the number of unique tiles that are part of any best path using iterative backtracking.
    """
    start = find_tile('start', maze)
    end = find_tile('end', maze)

    best_score, came_from = dijkstra_with_backtracking(maze, start, end)
    unique_tiles = set()

    # Aggregate all tiles from paths leading to valid end states
    for state in came_from.keys():
        if (state[0], state[1]) == end:
            unique_tiles.update(iterative_backtrack_paths(came_from, state))

    return len(unique_tiles)


# Load the maze
def open_maze(filename):
    """
    Reads the maze from the given file and returns it as a 2D list.
    """
    with open(filename, "r") as file:
        return [list(line.strip()) for line in file]


# Execute the solution with your maze input
reindeer_maze_part2 = open_maze("testinput.txt")
tile_count_iterative = count_unique_best_path_tiles_iterative(reindeer_maze_part2)
print(f"Number of tiles in the best paths: {tile_count_iterative}")
