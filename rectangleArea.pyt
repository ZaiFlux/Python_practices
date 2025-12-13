# How to get Rectangle Area

# function to calculate the area
def calculateArea(length, width):
    return length * width

length = float(input("Enter the length of the triangle: "))
width = float(input("Enter the width of the rectangel: "))

print(f"The are of given value {length} and {width} is: {round(calculateArea(length, width), 2)}cm")
