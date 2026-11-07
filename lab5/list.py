# List datatype: ordered, mutable, allows duplicates
nums = [10, 20, 30, 20]
mixed = [1, "two", 3.0, True]

print("nums  =", nums)
print("mixed =", mixed)
print("type(nums) :", type(nums))

print("nums[0]   :", nums[0])       # indexing
print("nums[-1]  :", nums[-1])      # last element
print("nums[1:3] :", nums[1:3])     # slicing

nums.append(40)                     # add at end
nums.insert(1, 15)                  # add at position
nums.remove(20)                     # remove first occurrence of value
print("after append/insert/remove :", nums)
print("popped :", nums.pop(), "->", nums)

print("sorted(nums)      :", sorted(nums))
print("nums reversed     :", nums[::-1])
print("len(nums)         :", len(nums))
print("20 in nums        :", 20 in nums)
print("[0]*3 + [1,2]     :", [0] * 3 + [1, 2])
