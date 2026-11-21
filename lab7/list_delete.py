# Delete or remove elements from a list
nums = [10, 20, 30, 20, 40]
print("nums        :", nums)

del nums[0]           # delete by index
print("del nums[0] :", nums)

nums.remove(20)       # remove the first matching value
print("remove(20)  :", nums)

last = nums.pop()     # remove and return the last item
print("pop()       :", nums, "| removed:", last)

first = nums.pop(0)   # remove and return the item at index 0
print("pop(0)      :", nums, "| removed:", first)

try:
    nums.remove(99)   # missing value -> ValueError
except ValueError as e:
    print("remove(99)  : ValueError:", e)

nums.clear()          # remove all items
print("clear()     :", nums)

# delete a range with a slice: the stop index is excluded
scores = [10, 20, 30, 40, 50]
del scores[1:3]       # removes index 1 and 2 (20 and 30)
print("del [1:3]   :", scores)
