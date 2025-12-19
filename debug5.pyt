def average(numbers):
    sum = 0
    for num in numbers:
        sum += num
    return sum / len(numbers)   # Bug here

students = ["Alice", "Bob", "Charlie"]
grades = [85, 90, 78]

for i in range(len(grades)):
    if grades[i] > 80:
        print(students[i], "passed with grade", grades[i])
    else:
        print(students[i], "failed with grade", grades[i])

print("Class average is:", average(grades))
