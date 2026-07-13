# lambda_functions.py
# Demonstrates lambda functions (small, unnamed functions written in one line)

# 1. Lambda function to add two numbers
add = lambda a, b: a + b
print("add(3, 4):", add(3, 4))

# 2. Lambda function to multiply two numbers
multiply = lambda a, b: a * b
print("multiply(3, 4):", multiply(3, 4))

# 3. Using a lambda with sorted() to sort a list by a custom key
students = [("John", 25), ("Mary", 19), ("Kwame", 22)]
# sort by age (the second item in each tuple)
sorted_students = sorted(students, key=lambda student: student[1])
print("Students sorted by age:", sorted_students)

# 4. Using filter() with a lambda: keep only even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda n: n % 2 == 0, numbers))
print("Even numbers:", even_numbers)

# 5. Using map() with a lambda: square every number in the list
squared_numbers = list(map(lambda n: n ** 2, numbers))
print("Squared numbers:", squared_numbers)