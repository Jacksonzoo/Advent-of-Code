# Open the input file and find a way to section the 'rules' and 'updates' so that we can differentiate the two
with open("input.txt", "r") as file:
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


# The goal is to look at the updats and see if they follow the 'rules' (X|Y) where page X at some point comes before page Y
# Disregarding the rules that do not apply, if the updates abide by the relevant rules record the middle page number
# Return the sum of all the middle page numebrs of the correctly ordered and rule abiding updates

total_pages = 0
correct_updates = []
incorrect_updates = []

for pages in updates:
    correct_order = True
    page = pages.split(",")

    for before, after in rules:
        if before in page and after in page:
            before_index = page.index(before)
            after_index = page.index(after)
            if before_index >= after_index:
                correct_order = False
                break

    if correct_order:
        middle_page = int(page[len(page) // 2])
        total_pages += middle_page
        correct_updates.append(page)
    else:
        incorrect_updates.append(page)


print(total_pages)


# For Part 2 of this problem, we now need to look at correctly order the updates that were not ordered in Part 1
# I would want to directly pull the ones that were not correctly ordered, then take a look at their applicable rules
# I would now use those rules to create a "new" update list that is now ordered correctly
# I would increment these values in a new counter and return the sum of the new middle pages

corrected_pages = 0

for page in incorrect_updates:
    new_order = list(page)
    correct_order = True
    while correct_order:
        correct_order = False
        for before, after in rules:
            if before in page and after in page:
                before_index = new_order.index(before)
                after_index = new_order.index(after)
                if before_index > after_index:
                    correct_order = True
                    new_order.remove(before)
                    new_order.insert(after_index, before)
                    
    middle_page = int(new_order[len(new_order) // 2])
    corrected_pages += middle_page

print(corrected_pages)
    

