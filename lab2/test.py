name = "manas"
age = 20

# wrong code print("my name is:name and my age is:age")

#right code
print("my name is", name, "and my age is", age)

#using f-string
print(f"my name is {name} and my age is {age}")


#percentile formatting
name2 ="mrd"
age2 = 21
cgpa = 9.5
print("name: %s, age: %d, cgpa: %.2f" % (name2, age2, cgpa))