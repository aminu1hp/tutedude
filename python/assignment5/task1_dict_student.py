students = {"Raja": 70, "Prada": 80}
name = input("Please enter the student\'s name: ")

marks = students.get(name)

if marks is None:
    print(name + " not found")
else:
    print(name + "\'s score is: ", marks)
