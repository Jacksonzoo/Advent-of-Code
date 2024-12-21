# Open the input file as a grid

def open_garden_map(filename):
    with open(filename, "r") as file:
        garden = [list(line.strip()) for line in file]
    return garden

# Part 1, given a garden there are regions of garden plots (represented by the same letters touching)
# Goal is to find how much the cost of fence would be sectioning each region
# Price of fense = perimeter * area of region where area is the number of letters in the region
# and perimeter is the number of fence faces surrounding each the region, given that each letter is a square shape

def check_in_garden(x, y, garden):
    return 0 <= x < len(garden) and 0 <= y < len(garden[0])


def track_region(garden):
    visited = set()
    regions = []
    direction = [
        (0, -1),        # left
        (-1, 0),        # up
        (0, 1),         # right
        (1, 0)          # down
    ]

    def bfs(start):
        queue = [start]
        area = 0
        perimeter = 0
        region_type = garden[start[0]][start[1]]
        region = set()

        while queue:
            x, y = queue.pop(0)
            if (x, y) in visited:
                continue
            visited.add((x, y))
            region.add((x, y))
            area += 1

            for dx, dy in direction:
                nx, ny = x + dx, y + dy
                if not check_in_garden(nx, ny, garden) or garden[nx][ny] != region_type:
                    perimeter +=1
                elif (nx, ny) not in visited:
                    queue.append((nx, ny))
        return region_type, area, perimeter
    
    for i in range(len(garden)):
        for j in range(len(garden[0])):
            if (i, j) not in visited:
                region_type, area, perimeter = bfs((i, j))
                regions.append((region_type, area, perimeter))
    return regions            


def find_fence_cost(regions):
    total_fence_cost = 0
    for region_type, area, perimeter in regions:
        total_fence_cost += area * perimeter
    return total_fence_cost
    

garden_map = open_garden_map("input.txt")
regions = track_region(garden_map)
total_cost = find_fence_cost(regions)
print(total_cost)





