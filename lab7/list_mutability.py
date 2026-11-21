# Lists are mutable: they can be changed in place
nums = [10, 20, 30]
print("nums       :", nums)
print("id before  :", id(nums))

nums[1] = 99       # change one item
nums.append(40)    # add an item
nums.pop(0)        # remove an item

print("nums after :", nums)
print("id after   :", id(nums))   # same id -> same list, changed in place

# A string is immutable: s stays the same, upper() makes a new string
s = "hello"
t = s.upper()
print("s          :", s)
print("t          :", t)
