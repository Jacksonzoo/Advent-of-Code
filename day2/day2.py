# open the input file and strip the data into an workable array

with open("input.txt","r") as file:
    content = file.readlines()

report_array = []

for levels in content:
    level = list(map(int, levels.split()))
    report_array.append(level)
print(report_array)


# now you need to find a way to iterate through each 'report' in the list, then through each 'level' in each 'report'
# with each iteration, you need to see if the numbers gradually increases/decreases by at least 1 but no more than 3 at a time
# if it does, have a dictionary that stores each value in 'safe' or 'unsafe' if it does not

result = {
    "safe" : 0,
    "unsafe" : 0
}

n = len(report_array)
for i in range(n):
    is_safe = True
    gradually = None
    for j in range(len(report_array[i]) - 1):
        difference = report_array[i][j] - report_array[i][j + 1]
        if 1 <= difference <= 3:
            if gradually == "increasing":
                is_safe = False
                break
            gradually = "decreasing"
        elif -3 <= difference <= -1:
            if gradually == "decreasing":
                is_safe = False
                break 
            gradually = "increasing"
        else:
            is_safe = False
            break
    if is_safe:
        result["safe"] += 1
    else:
        result["unsafe"] += 1

print(result)

# for part 2, a problem dampener is introduced in which we can take a look at the "unsafe" reports and retest them to see
# if they can become "safe" by removing just a single level from from each report
# by keeping the "safe" results redo part 1 but only for "unsafe" and see if removing just a single level can make it "safe"

new_result = {
    "safe" : 0,
    "unsafe" : 0
} 

for i in range(n):
    is_safe = True
    gradually = None
    for j in range(len(report_array[i]) - 1):
        difference = report_array[i][j] - report_array[i][j + 1]
        if 1 <= difference <= 3:
            if gradually == "increasing":
                is_safe = False
                break
            gradually = "decreasing"
        elif -3 <= difference <= -1:
            if gradually == "decreasing":
                is_safe = False
                break 
            gradually = "increasing"
        else:
            is_safe = False
            break
    if is_safe:
        new_result["safe"] += 1
    else:
        dampener = False
        for j in range(len(report_array[i])):
            unsafe_report = report_array[i][:j] + report_array[i][j + 1:]
            is_safe = True
            gradually = None
            for l in range(len(unsafe_report) - 1):
                difference = unsafe_report[l] - unsafe_report[l + 1]
                if 1 <= difference <= 3:
                    if gradually == "increasing":
                        is_safe = False
                        break
                    gradually = "decreasing"
                elif -3 <= difference <= -1:
                    if gradually == "decreasing":
                        is_safe = False
                        break
                    gradually = "increasing"
                else:
                    is_safe = False
                    break
            if is_safe:
                dampener = True
                break

        if dampener:
            new_result["safe"] += 1
        else:
            new_result["unsafe"] += 1

print(new_result)
