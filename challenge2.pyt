def sumAll(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

v = int(input("Enter a numbers to get the sum: "))

for i in range(1, v + 1):
    print(i)
print(f"The sum of 1 to {v} is {sumAll(v)}")