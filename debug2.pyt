# 🧩 Advanced Python Practice Challenge

# Function to reverse a string
def reverse_string(s):
    # Fill in the missing line
    return reversed(s)

# Function to count vowels in a string
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        # Fill in the missing line
        if char in vowels:
            count += 1
    return count

# Function to filter numbers greater than a threshold
def filter_greater(numbers, threshold):
    result = []
    for num in numbers:
        # Fill in the missing line
        if num > threshold:
            result.append(num)
    return result

# Function to create a dictionary from two lists
def create_dict(keys, values):
    my_dict = {}
    for i in range(len(keys)):
        # Fill in the missing line
          my_dict[keys[i]] = values[i]
    return my_dict

# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        # Fill in the missing conditional
        if n % i == 0:
            return False
    return True

# Main program
def main():
    text = "Programming is fun"
    numbers = [12, 7, 19, 4, 21, 3]

    print("Original text:", text)
    print("Reversed text:", reverse_string(text))
    print("Vowels in text:", count_vowels(text))

    threshold = 10
    print(f"Numbers greater than {threshold}:", filter_greater(numbers, threshold))

    keys = ["name", "age", "city"]
    values = ["Alice", 25, "Paris"]
    print("Dictionary:", create_dict(keys, values))

    print("Prime numbers in the list:")
    for num in numbers:
        # Fill in the missing line to print only prime numbers
        if is_prime(num) :
            print(num)

# Run the program
if __name__ == "__main__":
    main()
