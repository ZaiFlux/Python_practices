# Ask the user what number in multiplication table should be displayed.

num = int(input("Enter number here: "))

print(f"Multiplication table of {num} up to 10:")

for i in range(1, 11):
    result = num * i
    print(f"{num} x {i} = {result}")