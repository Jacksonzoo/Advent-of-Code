# Open the input file and find a way to section the 'rules' and 'updates' so that we can differentiate the two
with open("testinput.txt", "r") as file:
    rules = []
    updates = []
    section = 1
    for line in file:
        line = line.strip()
        if not line:
            section = 2
        elif section == 1:
            rules.append(line)
        else:
            updates.append(line)

print(f"Rules:", rules)
print(f"Updates:", updates)


# The goal is to look at the updats and see if they follow the 'rules' (X|Y) where page X at some point comes before page Y
# Disregarding the rules that do not apply, if the updates abide by the relevant rules record the middle page number
# Return the sum of all the middle page numebrs of the correctly ordered and rule abiding updates



