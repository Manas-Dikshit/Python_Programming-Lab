# Iteration in a list: for, while, range, enumerate, nested loops
names = ["Manas", "Ravi", "Suiit"]

# simple for loop over values
for name in names:
    print("Hello", name)

# while loop using an index
i = 0
while i < len(names):
    print("while:", i, names[i])
    i += 1

# range(len(list)) when the index is needed
for i in range(len(names)):
    print("index:", i, "->", names[i])

# enumerate gives index and value together
for i, name in enumerate(names):
    print("enum :", i, name)

# sum while iterating
nums = [1, 2, 3, 4]
total = 0
for n in nums:
    total += n
print("total:", total)

# nested lists: loop inside a loop
grid = [[1, 2], [3, 4]]
for row in grid:
    for item in row:
        print(item, end=" ")
print()

# comprehension is iteration too
print("doubled:", [n * 2 for n in nums])

# removing while iterating: loop over a copy
for n in nums[:]:
    if n % 2 == 0:
        nums.remove(n)
print("odds left:", nums)
