# Lists are mutable: they can be changed in place
nums = [10, 20, 30, 40]
print("nums       :", nums)
print("id before  :", id(nums))

nums[1] = 99       # change one item
nums.append(50)    # add an item
nums.pop(0)        # remove an item

# change two positions at a time
nums[0], nums[1] = 7, 8    # simultaneous assignment to two indexes
nums[2:4] = [5, 6]         # slice replaces two items with two new ones

print("nums after :", nums)
print("id after   :", id(nums))   # same id -> same list, changed in place

# A string is immutable: s stays the same, upper() makes a new string
s = "hello"
t = s.upper()
print("s          :", s)
print("t          :", t)
