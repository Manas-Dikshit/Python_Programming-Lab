# 30. Search a list with a while loop, break and while...else
items = ["book", "pen", "ruler", "pen"]

for target in ["pen", "eraser"]:
    index = 0
    while index < len(items):
        if items[index] == target:
            print(target, "found at", index)
            break
        index += 1
    else:
        print(target, "Not found")
