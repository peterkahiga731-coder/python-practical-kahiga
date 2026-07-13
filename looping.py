# 1. Print numbers from 1 to 20
print("Numbers from 1 to 20:")
for i in range(1, 21):
    print(i)

# 2. Multiplication table
num = int(input("Enter a number: "))
print("Multiplication Table:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# 3. Sum of numbers from 1 to 100 using while loop
total = 0
count = 1

while count <= 100:
    total += count
    count += 1

print("Sum of numbers from 1 to 100 is:", total)

# 4. Print even numbers between 1 and 50
print("Even numbers between 1 and 50:")
for i in range(2, 51, 2):
    print(i)