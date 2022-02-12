age = int(input("Age? "))

if age < 0:
    print("ERROR: invalid age!")
    exit(1)     # this terminates the program

print("Age:", age)

if (age < 13):
    cat = "child"

elif (age < 20):
    cat = "teenager"

else:
    cat = "adult"

print("Category:", cat)

