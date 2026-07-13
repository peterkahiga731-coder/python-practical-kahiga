# user_defined_functions.py
# Demonstrates writing your own (user-defined) functions

# 1. Function to add two numbers
def add_numbers(a, b):
    return a + b

# 2. Function to find the area of a rectangle
def rectangle_area(length, width):
    return length * width

# 3. Function to check if a number is prime
def is_prime(n):
    if n < 2:               # 0 and 1 are not prime numbers
        return False
    for i in range(2, n):   # check if anything between 2 and n-1 divides n evenly
        if n % i == 0:
            return False    # found a divisor -> not prime
    return True             # no divisors found -> prime

# 4. Function to find the factorial of a number (n! = n * (n-1) * ... * 1)
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i   # same as result = result * i
    return result

# 5. Function to display a student's details
def display_student(name, age, course, grade):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Course: {course}")
    print(f"Grade: {grade}")

# ---------- Testing all the functions ----------
print("add_numbers(5, 8):", add_numbers(5, 8))
print("rectangle_area(4, 6):", rectangle_area(4, 6))
print("is_prime(7):", is_prime(7))
print("is_prime(10):", is_prime(10))
print("factorial(5):", factorial(5))

print("\nStudent details:")
display_student("Ama Boateng", 20, "Computer Science", "A")