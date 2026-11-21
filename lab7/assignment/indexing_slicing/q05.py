# 5. Edit a list with slices
values = [10, 20, 30, 40, 50]
print("start        :", values)

values[1:4] = [200, 300]   # replace middle three items with two
print("after replace:", values)

del values[-2:]            # delete the last two items
print("after delete :", values)
