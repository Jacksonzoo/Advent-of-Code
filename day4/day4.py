# open the necessary file we are trying to solve for Day 4

with open("input.txt", "r") as file:
    puzzle = [line.strip() for line in file]

# search the problem and record every time 'XMAS' had appeared
# 'XMAS' could appear vertically, horizontally, diagonally, written backwards, or even overlapping (X for example)
# return the amount of times 'XMAS' was found in those conditions

xmas_count = 0
word = "XMAS"

directions = [
    (0, 1),   # right          horizontal  
    (0, -1),  # left           horizontal-backwards
    (1, 0),   # down           vertical
    (-1, 0),  # up             vertical-backwards
    (1, -1),  # down-left      diagonal-down-left
    (1, 1),   # down-right     diagonal-down-right
    (-1, 1),  # up-right       diagonal-up-right
    (-1, -1)  # up-left        diagona-up-left
]

for i in range(len(puzzle)):
    for j in range(len(puzzle[i])):
        if puzzle[i][j] != "X":
            continue
        for r, c in directions:
            row, col = i, j
            matching = True
            for k in range(len(word)):
                if not (0 <= row < len(puzzle) and 0 <= col < len(puzzle[0])):
                    matching = False
                    break
                if puzzle[row][col] != word[k]:
                    matching = False
                    break

                row += r
                col += c

            if matching:
                xmas_count += 1


print(xmas_count)

# For part 2 of the code, we are informed that the word search was not an 'XMAS' search; but an X-MAS search
# The task is now to search the puzzle to find 'MAS' in the shape of an X; where 'MAS' can be forward or backward

mas_count = 0

# For reference
    # (1, -1),  # down-left      diagonal-down-left
    # (1, 1),   # down-right     diagonal-down-right
    # (-1, 1),  # up-right       diagonal-up-right
    # (-1, -1)  # up-left        diagona-up-left


for i in range(len(puzzle)):
    for j in range(len(puzzle[i])):
        if puzzle[i][j] != "A":
            continue
        
        diagonal1 = False       #checking for \ diagonal
        if (0 <= i - 1 and 0 <= j - 1 and i + 1 < len(puzzle) and j + 1 < len(puzzle[0])):
            char1 = puzzle[i - 1][j - 1]    #looking at up-left
            char3 = puzzle[i + 1][j + 1]    #looking at down-right
            if (char1 == "M" and char3 == "S") or (char1 == "S" and char3 == "M"):
                diagonal1 = True
        
        diagonal2 = False       #checking for / diagonal
        if (0 <= i - 1 and 0 <= j - 1 and i + 1 < len(puzzle) and j + 1 < len(puzzle[0])):
            char1 = puzzle[i - 1][j + 1]    #looking at up-right
            char3 = puzzle[i + 1][j - 1]    #looking at down-left
            if (char1 == "M" and char3 == "S") or (char1 == "S" and char3 == "M"):
                diagonal2 = True
            
        if diagonal1 and diagonal2:
            mas_count += 1

print(mas_count)