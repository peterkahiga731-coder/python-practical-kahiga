# string.py
# This program demonstrates strings, concatenation,
# indexing, slicing, and string methods.

# Create string variables
first_name = "Prodbystones"
last_name = "Kahiga"

# Concatenation
full_name = first_name + " " + last_name
print("Full Name:", full_name)

# String indexing
print("First character:", full_name[0])
print("Last character:", full_name[-1])

# String slicing
print("First 5 characters:", full_name[0:5])
print("Last 6 characters:", full_name[-6:])

# String methods
print("Uppercase:", full_name.upper())
print("Lowercase:", full_name.lower())
print("Replace:", full_name.replace("Kahiga", "Student"))
print("Split:", full_name.split(" "))