# function to convert minutes into seconds.
def minutesTosec(minute):
    return minute * 60

# function to convert hours into minutes
def houtsTominutes(hours):
    return hours * 60


# the main
def main():
    while True:
        print("1. Minutes to seconds.") 
        print("2. Hours to minutes")
        print("3. Exit")

        choice = input("Enter your option: ")

        if choice == '1':
            minutes = int(input("Enter the minutes: "))
            result = minutesTosec(minutes)
            print(f"The seconds in {minutes} are {result} seconds")
        elif choice == '2':
            hours = int(input("Enter the hours: "))
            result = houtsTominutes(hours)
            print(f"The minutes in {hours} are {result} seconds.")
        elif choice == '3':
            print("Exiting")
            break
        else:
            print("Invalid input.")
        
        
main()