#Open input.txt into this file
with open("day1input.txt", "r") as f:
    contents = f.readlines()
    print(contents)

left_array = []
right_array = []

#split the two lists into a left list and right list
for line in contents:
    #numbers = line.strip()
    #print(numbers)
    left, right = map(int, line.split())
    left_array.append(left)
    right_array.append(right)

print(left_array)
print(right_array)

#sort both lists
n = len(left_array)
for i in range(n):
    for j in range(0, n - 1 - i):
        if left_array[j] > left_array[j + 1]:
            left_array[j], left_array[j + 1] = left_array[j + 1], left_array[j]
print(left_array)

m = len(right_array)
for i in range(m):
    for j in range(0, m - 1 - i):
        if right_array[j] > right_array[j + 1]:
            right_array[j], right_array[j + 1] = right_array[j + 1], right_array[j]
print(right_array)

#create a tempory list that would collect the difference in values between the two list
#point first index of left and first index of right // take difference and insert into new array
new = [abs(leftlist - rightlist) for leftlist, rightlist in zip(left_array, right_array)]
print(new)

#sum the values in the temporary list
answer = sum(new)
print(answer)
