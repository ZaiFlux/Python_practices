# 🧩 Python Practice Challenge

# Function to calculate the average of a list
def calculate_average(numbers):
    # Fill in the missing line to calculate the average
    average = sum(numbers) / len(numbers)
    return average

# Function to find the maximum number in a list
def find_max(numbers):
    max_num = numbers[0]
    for num in numbers:
        # Fill in the missing conditional to update max_num
        if num > max_num:
            max_num = num
    return max_num

# Function to display student scores
def display_scores(students, scores):
    for i in range(len(students)):
        # Fill in the missing print statement
        print(f"{students[i]}, {scores[i]}")

# Main program
def main():
    students = ["Alice", "Bob", "Charlie", "Diana"]
    scores = [85, 92, 78, 90]

    print("Student Scores:")
    display_scores(students, scores)

    avg_score = calculate_average(scores)
    print(f"\nAverage score: {avg_score}")

    max_score = find_max(scores)
    print(f"Highest score: {max_score}")

# Run the main program
if __name__ == "__main__":
    main()
