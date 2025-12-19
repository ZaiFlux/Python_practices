# Program: Simple Student Management System

# 1️⃣ Create an empty list to store students
students = []

# 2️⃣ Function to add a student
def add_student(name, score):
    # 3️⃣ Create a dictionary for one student
    student = {
        "name": name,
        "score": score
    }
    
    # 4️⃣ Add the student dictionary to the students list
    students.append(student)

# 5️⃣ Function to calculate average score
def calculate_average():
    # 6️⃣ Check if students list is empty
    if not students:
        return "No students found"
    
    total = 0
    
    # 7️⃣ Loop through each student in students
    for student in students:
        total = total + student["score"]
    
    # 8️⃣ Return the average
    return total / len(students)

# 9️⃣ Function to display all students
def display_students():
    # 🔟 Loop through students with index
    for i in range(len(students)):
        print(i + 1, "-", students[i]["name"], ":", students[i]["score"])

# 1️⃣1️⃣ Main program loop
while True:
    print("\nMENU")
    print("1. Add Student")
    print("2. View Students")
    print("3. View Average")
    print("4. Exit")
    
    # 1️⃣2️⃣ Get user choice
    choice = input("Enter choice: ")
    
    # 1️⃣3️⃣ If user wants to add student
    if choice == "1":
        name = input("Enter student name: ")
        score = float(input("Enter score: "))
        add_student(name, score)
        print("Student added!")
    
    # 1️⃣4️⃣ If user wants to view students
    elif choice == "2":
        display_students()
    
    # 1️⃣5️⃣ If user wants to see average
    elif choice == "3":
        avg = calculate_average()
        print("Average Score:", avg)
    
    # 1️⃣6️⃣ Exit condition
    elif choice == "4":
        print("Goodbye!")
        break
    
    # 1️⃣7️⃣ Invalid choice
    else:
        print("Invalid choice. Try again.")
