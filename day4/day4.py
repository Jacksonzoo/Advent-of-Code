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