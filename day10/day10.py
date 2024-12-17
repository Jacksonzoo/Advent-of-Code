# Open the file as a grid so we get our 'topographic topo_map'
def open_topo_map(filename):
    with open(filename, "r") as file:
        return [list(map(int, line.strip())) for line in file]


# An optimal hiking path is one where we start at height 0 and reach heigh 9 gradually increasing by 1
# A trailhead is the start of the trail, height of 0
# Trailhead score is the number of positions at height of 9 we can reach via an optimal path
# Find the trailscore for each trailhead and return the sum

def find_trailheads(grid):
    trailhead_position = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                trailhead_position.append((i ,j))
    return trailhead_position


def is_valid(x, y, grid):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0])


def trailhead_score(grid, start):
    directions = [
    (-1, 0),        # moving up
    (0, 1),         # moving right
    (1, 0),         # moving down
    (0, -1)         # moving left
]
    queue = [(start[0], start[1], 0)]
    visited = set()
    visited.add((start[0], start[1]))
    score = 0

    while queue:
        x, y, elevation = queue.pop(0)
        if elevation == 9:
            score += 1
            continue

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny, grid) and (nx, ny) not in visited:
                next_elevation = grid[nx][ny]
                if next_elevation == elevation + 1:
                    visited.add((nx, ny))
                    queue.append((nx, ny, next_elevation))

    return score


def total_score(grid):
    trailheads = find_trailheads(grid)
    total = 0
    for start in trailheads:
        total += trailhead_score(grid, start)
    return total
    

topo_map = open_topo_map("input.txt")

print(total_score(topo_map))


# For part 2, we now need to find the total number of unique paths we can take starting 
# at the trailhead of elevation 0, to reach the end at elevation 9

def unique_path_score (grid, start):
    directions = [
    (-1, 0),        # moving up
    (0, 1),         # moving right
    (1, 0),         # moving down
    (0, -1)         # moving left
]
    queue = [(start[0], start[1], 0)]
    unique_score = 0

    while queue:
        x, y, elevation = queue.pop()
        if elevation == 9:
            unique_score += 1
            continue

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny, grid):
                next_elevation = grid[nx][ny]
                if next_elevation == elevation + 1:
                    queue.append((nx, ny, next_elevation))
    return unique_score


def total_unique_score(grid):
    trailheads = find_trailheads(grid)
    unique_total = 0
    for start in trailheads:
        unique_total += unique_path_score(grid, start)
    return unique_total

print(total_unique_score(topo_map))

