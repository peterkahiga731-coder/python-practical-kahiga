# class_methods.py
# Demonstrates: constructor (__init__), instance variables, a class variable,
# and a class method (@classmethod)

class Student:
    # Class variable - shared by all Student objects
    school_name = "Greenfield High School"

    # Constructor - runs when a new object is created
    def __init__(self, name, age):
        self.name = name   # instance variable - unique to this object
        self.age = age      # instance variable - unique to this object

    # A normal instance method - works with one specific object (self)
    def display_info(self):
        print(f"{self.name} ({self.age} years old) attends {Student.school_name}")

    # A CLASS method - works with the CLASS itself, not one object.
    # "cls" refers to the class (Student), similar to how "self" refers to an object.
    @classmethod
    def change_school(cls, new_name):
        cls.school_name = new_name   # updates the class variable for ALL students


# ---------- Demonstrate how it works ----------
student1 = Student("Kofi Owusu", 18)
student2 = Student("Abena Serwaa", 17)

student1.display_info()
student2.display_info()

# Call the class method to change the school name for everyone at once
print("\nChanging school name using the class method...")
Student.change_school("Unity Senior High")

student1.display_info()
student2.display_info()