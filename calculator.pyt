operator = input("Enter the operator (+, -, /, *):")

val1 = float(input("Enter the value 1: "))
val2 = float(input("Enter the value 2: "))

if operator == '+':
    result = val1 + val2
    print(f"{val1} + {val2} = {result}")
elif operator == '-':
    result = val1 - val2
    print(f"{val1} - {val2} = {result}")
elif operator == '/':
    result = val1 / val2
    print(f"{val1} / {val2} = {int(result)}")
elif operator == '*':
    result = val1 * val2
    print(f"{val1} * {val2} = {result}")
else: 
    print("INVALID INPUT")