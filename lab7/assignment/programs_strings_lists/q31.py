# 31. Menu program for a reading list
reading = []

while True:
    print("\n1 Add  2 Remove  3 Search  4 Display  5 Exit")
    choice = input("Choose: ").strip()

    if choice == "1":
        title = input("Title: ").strip()
        if title:
            reading.append(title)
        else:
            print("Empty title rejected")
    elif choice == "2":
        title = input("Title: ").strip()
        if title in reading:
            reading.remove(title)
        else:
            print("Not found")
    elif choice == "3":
        title = input("Title: ").strip()
        print("Found" if title in reading else "Not found")
    elif choice == "4":
        for i, title in enumerate(reading, 1):
            print(i, title)
    elif choice == "5":
        break
    else:
        print("Invalid choice")
