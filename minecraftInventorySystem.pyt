# MINECRAFT Inventory System

# Inventory container
Inventory = []

# ---------------------------
# Function to add item
# ---------------------------
def addItem():
    itemName = input("Enter the item to add: ")
    quantity = input("Enter how many: ")
    value = float(input("Enter the value: "))

    Inventory.append({
        "Item": itemName,
        "Quantity": quantity,
        "Value": value
    })

    print(f"{itemName} was successfully added to the inventory\n")


# ---------------------------
# Function to view inventory
# ---------------------------
def viewInventory():
    if not Inventory:
        print("Inventory is empty\n")
        return

    print("Current Inventory:")
    for i, item in enumerate(Inventory, start=1):
        print(f"{i}. Item: {item['Item']}, Quantity: {item['Quantity']}, Value: {item['Value']}")
    print("")


# ---------------------------
# Function to search for an item
# ---------------------------
def searchItem():
    itemName = input("Enter the item name to find: ")
    found = False
    for item in Inventory:
        if item["Item"].lower() == itemName.lower():
            found = True
            print(f"Found: Name: {item['Item']}, Quantity: {item['Quantity']}, Value: {item['Value']}\n")
            break

    if not found:
        print(f"{itemName} was not in the inventory\n")


# ---------------------------
# Function to update an item
# ---------------------------
def updateItem():
    itemName = input("Enter the name of the item to update: ")
    found = False

    for item in Inventory:
        if item["Item"].lower() == itemName.lower():
            found = True
            print(f"Current: Name: {item['Item']}, Quantity: {item['Quantity']}, Value: {item['Value']}")

            newItem = input("Enter the new name (press Enter to keep current): ")
            newQuantity = input("Enter new quantity (press Enter to keep current): ")
            newValue = input("Enter new value (press Enter to keep current): ")

            if newItem:
                item["Item"] = newItem
            if newQuantity:
                item["Quantity"] = int(newQuantity)
            if newValue:
                item["Value"] = float(newValue)

            print(f"{itemName} was successfully updated in the inventory\n")
            break

    if not found:
        print(f"{itemName} was not found in the inventory\n")


# ---------------------------
# Function to delete an item
# ---------------------------
def deleteItem():
    itemName = input("Enter the name of the item to delete: ")
    found = False

    for item in Inventory:
        if item["Item"].lower() == itemName.lower():
            found = True
            Inventory.remove(item)
            print(f"{itemName} was successfully deleted from the inventory\n")
            break

    if not found:
        print(f"{itemName} was not found in the inventory\n")


# ---------------------------
# Main Menu
# ---------------------------
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
            addItem()
        elif choice == "2":
            viewInventory()
        elif choice == "3":
            searchItem()
        elif choice == "4":
            updateItem()
        elif choice == "5":
            deleteItem()
        elif choice == "6":
            print("Exiting Inventory System...")
            break
        else:
            print("Invalid choice! Please try again.\n")


# Run the program
if __name__ == "__main__":
    main()
