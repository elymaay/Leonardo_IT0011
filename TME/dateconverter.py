# Function to convert date from mm/dd/yyyy to human-readable format
def convert_date(date_input):
    # Extract month, day, and year
    month = int(date_input[0:2]) # Takes characters from index 0 to 1 
    day = int(date_input[3:5]) # Takes characters from index 3 to 4 
    year = int(date_input[6:]) # Takes characters from index 6 to the end of the string

    # List of month names
    months = ["January", "February", "March", "April", "May", "June", 
              "July", "August", "September", "October", "November", "December"]

    # Get the month name
    month_name = months[month - 1]

    # Return the formatted date
    return f"{month_name} {day}, {year}"

# Ask the user for input
date_input = input("Enter the date (mm/dd/yyyy): ")

# Convert the date and print the result
try:
    date_output = convert_date(date_input)
    print(f"Date Output: {date_output}")
except Exception as e:
    print("Invalid date format. Please use mm/dd/yyyy.")