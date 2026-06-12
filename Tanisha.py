students=["Tapish","Anamika","Riya","Suhana"]

k=input("Enter new student:")
students.append(k)

print(students)

s= input("Search Student:")
if s in students:
    print("Student found.\n")
else:
    print("Student not found.\n")

m=input("Remove student name:")
try:
    students.remove(m)
except ValueError:
    print("Student is not in the list.\n")

print(students)
