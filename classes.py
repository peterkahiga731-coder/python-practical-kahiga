# classes.py
# Demonstrates a basic class with attributes (no class variables/class methods yet)

class Student:
    # The constructor runs automatically when a new Student object is created
    def __init__(self, name, admission_number, course):
        self.name = name
        self.admission_number = admission_number
        self.course = course

    # A method to display this student's information
    def display_info(self):
        print(f"Name: {self.name}, Admission No: {self.admission_number}, Course: {self.course}")


# ---------- Create at least three Student objects ----------
student1 = Student("Kojo Mensah", "SC001", "Computer Science")
student2 = Student("Adwoa Owusu", "SC002", "Information Technology")
student3 = Student("Yaw Darko", "SC003", "Software Engineering")

# ---------- Display their information ----------
student1.display_info()
student2.display_info()
student3.display_info()