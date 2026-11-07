# Dictionary datatype: key -> value pairs, mutable, keys must be unique
student = {"name": "Manas", "age": 19, "cgpa": 8.5}

print("student    =", student)
print("type(student) :", type(student))

print("student['name'] :", student["name"])          # KeyError if missing
print("student.get('branch') :", student.get("branch"))  # None if missing
print("student.get('branch', 'CSE') :", student.get("branch", "CSE"))

student["branch"] = "CSE"      # add
student["age"] = 20            # update
del student["cgpa"]            # delete
print("after changes :", student)

print("keys()   :", list(student.keys()))
print("values() :", list(student.values()))
print("items()  :", student.items())

for key, value in student.items():
    print("  ", key, "->", value)

print("len(student) :", len(student))
print("'name' in student :", "name" in student)
