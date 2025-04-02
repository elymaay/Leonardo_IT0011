import csv  # Import the CSV module

# Open and read the CSV file
with open('currency.csv', mode='r', newline='') as file:
    reader = csv.reader(file)  
    exchange_rates = {}  # Dictionary to store rates
    try:
        with open(currency.csv, mode='r', newline='') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            for row in reader:
                if len(row) >= 2:
                    currency = row[0].strip()
                    try:
                        rate = float(row[1].strip())  # Convert rate to float
                        exchange_rates[currency] = rate
                    except ValueError:
                        pass  # Ignore if conversion fails
    except FileNotFoundError:
        print("File not found!")
    return exchange_rates

# Function to convert currency
def convert_currency(usd_amount, currency, exchange_rates):
    if currency in exchange_rates:
        return usd_amount * exchange_rates[currency]
    else:
        return None  # If currency not found

# Main program
filename = 'currency.csv'  # CSV file name
rates = load_exchange_rates(filename)  # Load rates

# Ask user for input
dollar = input("How much dollar do you have? ")
try:
    dollar = float(dollar)  # Convert input to float
except ValueError:
    print("Invalid input! Enter a number.")
    exit()

currency = input("What currency do you want to have? ").upper().strip()

converted_amount = convert_currency(dollar, currency, rates)
if converted_amount is not None:
    print(f"\nDollar: {dollar} USD")
    print(f"{currency}: {converted_amount}")
else:
    print("Currency not found in the list.")
