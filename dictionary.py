# dictionary.py
# This program demonstrates a Python dictionary.

# Create a dictionary
student = {
    "Name": "Prodbystones",
    "Age": 20,
    "Course": "Computer Science"
}

# Display the dictionary
print("Student Information")
print(student)

# Access values
print("Name:", student["Name"])
print("Age:", student["Age"])
print("Course:", student["Course"])

# Add a new key-value pair
student["University"] = "Cooperative University"

print("Updated Dictionary:")
print(student)