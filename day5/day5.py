# Open the input file and find a way to section the 'rules' and 'updates' so that we can differentiate the two
with open("testinput.txt", "r") as file:
    rules_temp = []
    updates = []
    section = 1
    for line in file:
        line = line.strip()
        if not line:
            section = 2
        elif section == 1:
            rules_temp.append(line)
        else:
            updates.append(line)
    
    rules = [tuple(item.split("|")) for item in rules_temp]

print(f"Rules:", rules)
print(f"Updates:", updates)


# The goal is to look at the updats and see if they follow the 'rules' (X|Y) where page X at some point comes before page Y
# Disregarding the rules that do not apply, if the updates abide by the relevant rules record the middle page number
# Return the sum of all the middle page numebrs of the correctly ordered and rule abiding updates

total_pages = 0

for before, after in rules:
    for pages in updates:
        correct_order = True
        page = pages.split(",")
        if before in page and after in page:
            before_index = page.index(before)
            after_index = page.index(after)
            if before_index < after_index:
                continue
            else:
                correct_order = False
                break
            print(correct_order)
        if correct_order:
            middle_page = int(pages[len(pages) // 2])
            total_pages += middle_page

print(total_pages)
