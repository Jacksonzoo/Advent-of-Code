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


# Part 2, a discount is introduced for buying the fences in bulk. Instead of using the 
# perimeter when considering the price we can now consider the number of sides the regions have.
# Consider a 2x2 grid. As opposed to having a fence cost of $32 (perimeter (8) * area (4))
# we now have a fence price of $16 (side (4) * area (4))


def get_corners(x, y, garden, plant_type):
    directions = [
        (-1, -1,), (-1, 0), (-1, 1),    # NW, N, NE
        (0, -1),            (0, 1),     # W,     E
        (1, -1),  (1, 0),   (1, 1)      # SW, S, SE
    ]

    adjacent = [
        check_in_garden(x + dx, y+ dy, garden) and garden[x + dx][y + dy] == plant_type
        for dx, dy in directions
    ]

    NW, N, NE, W, E, SW, S, SE = adjacent
    return sum([
        N and W and not NW, 
        N and E and not NE,
        S and W and not SW,
        S and E and not SE,
        not (N or W),
        not (N or E),
        not (S or W),
        not (S or E)
    ])

def find_region(x, y, garden):
    plant_type = garden[x][y]
    region = set()
    queue = [(x, y)]

    while queue:
        cx, cy = queue.pop()
        if (cx, cy) in region:
            continue
        region.add((cx, cy))

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = cx + dx, cy + dy
            if(
                check_in_garden(nx, ny, garden)
                and garden[nx][ny] == plant_type
                and (nx, ny) not in region
                and (nx, ny) not in queue
            ):
                queue.append((nx, ny))

    corners = sum(get_corners(rx, ry, garden, plant_type) for rx, ry in region)
    return region, corners * len(region)

def calc_discounted_cost(garden):
    visited = set()
    total_cost = 0

    for x in range(len(garden)):
        for y in range(len(garden[0])):
            if (x, y) not in visited:
                region, cost = find_region(x, y, garden)
                total_cost += cost
                visited |= region
    return total_cost


garden_map_two = open_garden_map("input.txt")
discounted_cost = calc_discounted_cost(garden_map_two)
print(discounted_cost)

