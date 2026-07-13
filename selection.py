# selection.py
# Demonstrates: if, if...else, and if...elif...else statements

# ---------- 1. Simple "if" example ----------
temperature = 30
if temperature > 25:
    print("It's a hot day.")  # only runs when the condition is True

# ---------- 2. "if...else" example: pass or fail based on score ----------
score = 45  # try changing this value to test both branches

if score >= 50:
    print("Result: You passed!")
else:
    print("Result: You failed.")

# ---------- 3. "if...else" example: check even or odd ----------
number = int(input("Enter a number to check if it's even or odd: "))

if number % 2 == 0:   # % is the modulus operator - gives the remainder after division
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")

# ---------- 4. "if...elif...else" example: find the largest of three numbers ----------
a = 12
b = 45
c = 27

if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

print(f"The largest number among {a}, {b}, {c} is {largest}")