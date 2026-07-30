# Student Club Management System
# This project demonstrated Python set operations:
# Union, Intersection, Difference, and Membership checking.

# Creating student groups
python_students = {"Ali", "Ahmed", "Sara", "John"}
web_students = {"Ahmed", "Sara", "Mike", "Emma"}

# Find students who are in both clubs
both_clubs = python_students & web_students

print("Students in both clubs")
print(both_clubs)

# Find students only in Python club
python_only = python_students - web_students

print("Students only in Python club")
print(python_only)

# Check student membership
student = input("Enter student name:")

if student in python_students:
    print(student, "is in Python club")
else:
    print(student, "is not in Python club")

# User input
club = input("Enter club name(Python/Web):")

if club.lower() == "python":
    print(student in python_students)

elif club.lower() == "web":
    print(student in web_students)
    
else:
    print("Invalid club name.")