# All 11 list methods in one program
nums = [1, 2, 2, 3]
print("start        :", nums)

# len() is a built-in function, not a list method
print("len(nums)    :", len(nums))
print("len([1,2,3]) :", len([1, 2, 3]))

nums.append(4)              # add at the end
print("append(4)    :", nums)

nums.insert(1, 9)           # add at a given index
print("insert(1, 9) :", nums)

nums.extend([5, 6])         # add every item from another list
print("extend([5,6]):", nums)

print("count(2)     :", nums.count(2))
print("index(3)     :", nums.index(3))

nums.remove(9)              # remove first matching value
print("remove(9)    :", nums)

print("pop()        :", nums.pop(), "->", nums)     # remove last
print("pop(0)       :", nums.pop(0), "->", nums)    # remove by index

nums.reverse()
print("reverse()    :", nums)

nums.sort()
print("sort()       :", nums)

copy = nums.copy()
print("copy()       :", copy, "| same object:", copy is nums)

copy.clear()
print("clear()      :", copy, "| nums intact:", nums)
print("len(copy)    :", len(copy))

# sort() with options
words = ["apple", "kiwi", "banana"]
words.sort(key=len)
print("sort(key=len):", words)
words.sort(reverse=True)
print("sort(reverse):", words)
