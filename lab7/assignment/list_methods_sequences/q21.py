# 21. Remove items with remove(), pop() and clear()
nums = [10, 20, 20, 30]
print("start:", nums)

nums.remove(20)                 # first matching value
print("after remove(20):", nums)

removed = nums.pop(1)           # by index
print("pop(1) removed:", removed, "| list:", nums)

removed = nums.pop()            # last item
print("pop() removed :", removed, "| list:", nums)

nums.clear()
print("after clear():", nums)
