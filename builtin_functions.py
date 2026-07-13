# builtin_functions.py
# Demonstrates at least 10 built-in Python functions

numbers = [4, 9, 1, 7, 3]

# 1. len() - number of items in a list
print("len(numbers):", len(numbers))

# 2. max() - largest value
print("max(numbers):", max(numbers))

# 3. min() - smallest value
print("min(numbers):", min(numbers))

# 4. sum() - total of all values
print("sum(numbers):", sum(numbers))

# 5. type() - shows the data type of a value
print("type(numbers):", type(numbers))

# 6. sorted() - returns a NEW sorted list (does not change the original)
print("sorted(numbers):", sorted(numbers))

# 7. abs() - absolute (positive) value of a number
print("abs(-15):", abs(-15))

# 8. round() - rounds a number to the nearest whole number (or given decimals)
print("round(3.7):", round(3.7))
print("round(3.14159, 2):", round(3.14159, 2))

# 9. input() - takes text typed by the user (always returns a string)
name = input("Enter your name: ")
print("Hello,", name)

# 10. print() - displays output to the screen (used throughout this file)
print("This whole file used print() to show its results.")