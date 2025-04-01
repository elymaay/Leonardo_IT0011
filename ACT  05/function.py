while True:
    print("\nMenu:")
    print("[D] - Divide")
    print("[E] - Exponentiation")
    print("[R] - Remainder")
    print("[F] - Summation")
    print("[X] - Exit")
    
    choice = input("Enter choice: ").upper()
    
    if choice == 'D':
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if num2 == 0:
            print("Denominator cannot be zero.")
            print(None)
        else:
            print("Result:", num1 / num2)
    
    if choice == 'E':
        num1 = float(input("Enter base number: "))
        num2 = float(input("Enter exponent: "))
        print("Result:", num1 ** num2)
    
    if choice == 'R':
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        if num2 == 0:
            print("Denominator cannot be zero.")
            print(None)
        else:
            print("Result:", num1 % num2)
    
    if choice == 'F':
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        if num2 <= num1:
            print("Second number must be greater than first number.")
            print(None)
        else:
            total = 0
            for i in range(num1, num2 + 1):
                total += i
            print("Result:", total)
    
    if choice == 'X':
        print("Exiting...")
        break
    
    if choice not in ['D', 'E', 'R', 'F', 'X']:
        print("Invalid choice, please try again.")
