students = []

for i in range(3):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))

    if marks >= 75:
        grade = "A"
    elif marks >= 65:
        grade = "B"
    elif marks >= 50:
        grade = "C"
    else:
        grade = "F"

    students.append((name, marks, grade))

print("\nStudent Results")

for s in students:
    print("Name:", s[0], "| Marks:", s[1], "| Grade:", s[2])