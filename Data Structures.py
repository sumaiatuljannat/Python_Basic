students = ["Sumaia", "Jannat", "Naima", "Tultul", "Mazumder"]

scores = [45, 67, 88, 78, 64, 72, 81]

print(students[0])
print(students[2])
print(students[-1])
print(students[-2])

print(scores[-1])
print(scores[-3])

print(scores[0:3])
print(scores[2:5])
print(scores[:3])

print(scores[::2])
print(scores[::-1])

print(scores[-3:])


#tupple
student_record=("Sumaia",21,3.5,"CSE")
print(student_record[0])
print(student_record[-1])
print(student_record[1:3])

 #Dictionary
student = {
    "name": "Sumaia",
    "age": 21,
    "gpa": 3.5,
    "enrolled": True
}
print(student["name"])
print(student.get("age"))
print(student.get("gpa"))
print(student.get("email", "N/A"))
