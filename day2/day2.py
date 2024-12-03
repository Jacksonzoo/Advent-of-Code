#open the input file and strip the data into an workable array
with open("testinput.txt","r") as file:
    content = file.readlines()

report_array = []

for levels in content:
    level = list(map(int, levels.split()))
    report_array.append(level)
print(report_array)


#now you need to find a way to iterate through each 'report' in the list, then through each 'level' in each 'report'
#with each iteration, you need to see if the numbers gradually increases/decreases by at least 1 but no more than 3 at a time
#if it does, have a dictionary that stores each value in 'safe' or 'unsafe' if it does not

result = {
    "safe" : 0,
    "unsafe" : 0
}

n = len(report_array)
for i in range(n):
    for j in range(len(report_array[i])):
        for k in range(report_array[i][j]):
            