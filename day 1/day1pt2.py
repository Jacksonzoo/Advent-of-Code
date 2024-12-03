#split the list into left and right portions
with open("day1input2.txt", "r") as f:
    content = f.readlines()

left_array = []
right_array = []

for line in content:
    number = line.strip()
    left, right = line.split()
    left_array.append(left)
    right_array.append(right)

print(left_array)
print(right_array)

dict = {}

p = len(right_array)
for i in range(0, p):
    if right_array[i] not in dict:
        dict[right_array[i]] = 1
    else:
        dict[right_array[i]] += 1

l = len(left_array)
total = 0
for i in range(0, l):
    if left_array[i] in dict:
        freq = int(left_array[i]) * dict[left_array[i]]
        print(freq)
        total +=freq
print(total)
