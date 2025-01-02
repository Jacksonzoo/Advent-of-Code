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

from sys import argv
from heapq import heappop, heappush
from math import inf

with open(argv[1]) as f:
    lines = [l.strip() for l in f]

dimx, dimy = (len(lines[0]), len(lines))
maze = list("".join(lines))
start, end = (maze.index("S"), maze.index("E"))
dirs = [-dimx, 1, dimx, -1]

visited = dict()
q = list()
highscore = inf
paths = list()

heappush(q, (0, start, 1, ""))
while q:
    score, pos, d, path = heappop(q)
    if score > highscore:
        break
    if (pos, d) in visited and visited[(pos, d)] < score:
        continue
    visited[(pos, d)] = score
    if pos == end:
        highscore = score
        paths.append(path)
    if maze[pos+dirs[d]] != "#":
        heappush(q, (score+1, pos+dirs[d], d, path+"F"))
    heappush(q, (score+1000, pos, (d+1)%4, path+"R"))
    heappush(q, (score+1000, pos, (d-1)%4, path+"L"))

tiles = set()
tiles.add(start)
for p in paths:
    t, d = (start, 1)
    for c in p:
        if c=="L": d=(d-1)%4
        elif c=="R": d=(d+1)%4
        elif c=="F":
            t+=dirs[d]
            tiles.add(t)
print(f"Shortest path: {highscore}")
print(f"Optimal viewing positions: {len(tiles)}")