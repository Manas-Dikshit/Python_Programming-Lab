# List operations: create, add, remove, search, sort, copy, iterate
nums = [10, 20, 30, 20]

# Creation and length
print("nums         :", nums)
print("type(nums)   :", type(nums))
print("len(nums)    :", len(nums))
print("list('abc')  :", list("abc"))
print("list(range(5)):", list(range(5)))

# Add: append / extend / insert
nums.append(40)
nums.extend([50, 60])
nums.insert(1, 15)
print("after add    :", nums)

# Search: index / count / in
print("nums.index(20):", nums.index(20))
print("nums.count(20):", nums.count(20))
print("30 in nums   :", 30 in nums)

# Remove: remove / pop / del / clear
nums.remove(20)              # first occurrence by value
last = nums.pop()            # last item by index
nums.pop(0)                  # item at index 0
del nums[1]                  # del statement
print("removed      :", nums, "| popped:", last)

copy = nums.copy()           # same as nums[:] or list(nums)
copy.clear()
print("copy cleared :", copy, "| nums intact:", nums)

# Order: sort / reverse (in place) vs sorted() (new list)
order = [3, 1, 2]
print("sorted(order):", sorted(order))
print("reversed     :", list(reversed(order)))
order.sort()
order.reverse()
print("after sort+rev:", order)
print("min/max/sum  :", min(order), max(order), sum(order))

# Iterate: enumerate / zip / comprehension
names = ["Manas", "Ravi"]
marks = [91, 88]
print("enumerate    :", [(i, name) for i, name in enumerate(names)])
print("zip          :", list(zip(names, marks)))
print("squares      :", [x * x for x in range(6)])
print("evens        :", [x for x in range(10) if x % 2 == 0])

# Nested lists
grid = [[1, 2], [3, 4]]
print("grid[1][0]   :", grid[1][0])
