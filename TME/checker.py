# Open the file "numbers.txt" and read the lines
file_path = r"C:\Users\ELY\Downloads\numbers.txt" 
with open(file_path, "r") as file:
    lines = file.readlines()
# Function to check if a number is a palindrome
# Function to check if a number is a palindrome
def is_palindrome(number):
    number_str = str(number)
    return number_str == number_str[::-1]

# Process each line in the file
for line in lines:
    # Remove any whitespace characters 
    line = line.strip()

    # To separate the numbers, split the line by commas
    numbers = line.split(",")

    # Convert each number to an integer and sum them
    total = 0
    for num in numbers:
        if num.strip():  # Only process non-empty strings
            total += int(num)

    # Check if the sum is a palindrome
    if is_palindrome(total):
        print(f"The sum of {line} is {total}, which is a palindrome.\n")
    else:
        print(f"The sum of {line} is {total}, which is not a palindrome.\n")