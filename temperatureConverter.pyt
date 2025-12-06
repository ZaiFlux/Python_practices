# Temperature Converter

print("Choose what you want to convert:")
print("1. Celcius to Fahrenheit")
print("2. Fahrenheit to Celcius")
print("")
converter = int(input("Enter here what you want to convert: "))

temp = float(input("Enter the value here: "))

if converter == 1:
    result = (temp - 32) * 5.0 / 9.0
    print(f"the temperature {temp} in Fahrenheit is {round(result, 2)}°F")
elif converter == 2:
    result = (temp * 9 / 5) + 32 
    print(f"the temperature {temp} in Celcius  is {round(result, 2)}°C")



