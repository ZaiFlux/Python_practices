# first create a container for the students
students = {}

# create a function to add the student
def addStudent():
    name = input("Enter the name of the student: ")
    score = float(input(f"Enter {name}'s score: "))
    students[name] = score

# function to view added students
def viewStudents():
    if not students:
        print("Student list is empty")
    else:
        print("Student Records: ")
        for name, score in students.items():
            print(f"{name}: {score}")
            print("")
# function to search students in the list
def searchStudents():
    name = input("Enter name of the student to find: ")
    if name in students:
        print(f"{name} {students[name]}\n")
    else: 
        print(f"No {name} found\n")

#function to update the students in the list
def updateStudents():
    name = input("Enter the of the students to update: ")
    if name in students:
        score = input(f"Enter new score for  {name}: ")
        students[name] = score
        print(f"{name}'s score is updated to {score}")
    else:
        print(f"{name} not found")

#function to delete the students in the list
def deleteStudents():
    name = input("Enter the name to delete the student in the list")
    if name in students:
        del students[name]
        print(f"{name} record was successfully deleted\n")
    else: 
        print(f"{name}'s record not found")


def main():
        while True:
            print("STUDENT SCORE MANAGER")
            print("1. Add student")
            print("2. View student")
            print("3. Search Student")
            print("4. Update student")
            print("5. Delete student")
            print("6. Exit")

            choice = input("Enter your choice: ")
            print ()
            if choice == '1':
                addStudent()
            elif choice == '2':
                viewStudents()
            elif choice == '3':
                searchStudents()
            elif choice == '4':
                updateStudents()
            elif choice =='5':
                deleteStudents()
            elif choice == '6':
                print("Extiting the program")
                break
            else:
                print("Invalid Input")

if __name__ == "__main__":
    main()




