# 23. Sort and reverse a list; note which operations mutate it
nums = [30, 10, 20, 10]

ascending = sorted(nums)        # new list, original unchanged
print("sorted copy:", ascending, "| original:", nums)

nums.sort(reverse=True)         # in place
print("after sort(reverse=True):", nums)

nums.reverse()                  # in place
print("after reverse():", nums)
