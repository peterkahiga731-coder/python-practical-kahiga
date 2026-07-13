# class_variables.py
# Demonstrates a class variable - a value shared by ALL objects of a class

class Student:
    # This is a CLASS variable - it belongs to the class itself,
    # not to any single object. Every Student shares the same value.
    school_name = "Greenfield High School"

    def __init__(self, name, course):
        # These are INSTANCE variables - each object gets its own copy
        self.name = name
        self.course = course


# ---------- Create different Student objects ----------
student1 = Student("Efua Asante", "Business Administration")
student2 = Student("Nana Boateng", "Engineering")

# ---------- Access the class variable from different objects ----------
print(f"{student1.name} attends {student1.school_name}")
print(f"{student2.name} attends {student2.school_name}")

# Also accessible directly from the class itself
print("Accessed from the class directly:", Student.school_name)

# If we change it using the class name, it changes for every object
Student.school_name = "Unity Senior High"
print(f"\nAfter update -> {student1.name} attends {student1.school_name}")
print(f"After update -> {student2.name} attends {student2.school_name}")