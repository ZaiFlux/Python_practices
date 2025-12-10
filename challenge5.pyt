#Reverse a String

def str(text):
    reversed_text = ""
    for char in text:
        reversed_text = char + reversed_text
    return reversed_text 
              

string = input("Enter a string here: ")

print(f"Before: {string}")
print(f"After: {str(string)}") 