# container of the scores
scores = []

#function to sotre scores of the students
def addScore ():
    stuName = input("Enter the student name: ")
    score = input("Enter the score of the student to add: ")
    item = int(input("How many item is the exam: "))

    scores.append({
        "Name" : stuName,
        "Score" : score,
        "Item"  : item
    })

    print(f"You succesfully added the {stuName}")

# funtion to view all students scores
def viewScore():
    if not scores:
        print("Student list is empty.")
    return

print("Current Student:\n")
for i, item in enumerate(scores, start = 1):
    print(f"Student name: {item["Name"]}, Score: {item["Score"]}, Item: {item["Item"]}")
    print("")

#function to search the student record
def searchStu():
    stuName = input("Enter the student name to find:")
    print("No studet found")
    found = False

    for item in scores:
        if item["Name"].lower() == stuName.lower():
            found = True
            print(f"Student name: {item["Name"]}, Score: {item["Score"]}, Item: {item["Item"]}")
            break
        if not found:
            print(f"{stuName} not found, no data")
        
# function to update the student record
def updateSccore():
    stuName = input("Enter the student name to update")
    found = False

    for item in scores:
        if item["Name"].lower() == stuName.lower():
            found = True
            print(f"Student name: {item["Name"]}, Score: {item["Score"]}, Item: {item["Item"]}")
            break
        if not found:
            print(f"{stuName} not found no data.")

# function to remove the student record
def removeScore():
    stuName = input("Enter the student name to delete record")
    found = False

    for item in scores:
        if item["Name"].lower() == stuName.lower():
            found = True

            scores.remove(item)
            print("f{stuName} record was succesfully deleted")
            break
        
        if not found:
            print(f"{stuName} record was not found, no data")

# function for mainMeNU
def main():
    while True:
        print("=== Minecraft Inventory System ===")
        print("1. Add Item")
        print("2. View Inventory")
        print("3. Search Item")
        print("4. Update Item")
        print("5. Delete Item")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            addScore()
        elif choice == "2":
            viewScore()
        elif choice == "3":
            searchStu()
        elif choice == "4":
            updateSccore()
        elif choice == "5":
            removeScore()
        elif choice == "6":
            print("Exiting Inventory System...")
            break
        else:
            print("Invalid choice! Please try again.\n")


# Run the program
if __name__ == "__main__":
    main()
