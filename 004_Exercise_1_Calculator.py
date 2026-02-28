import math

while True:
    try:
        num1 = float(input("Enter the first number: "))
        operator = input("Enter the operator (+, -, *, /): ")
        num2 = float(input("Enter the second number: "))

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Error! Division by Zero."
        else:
            result = "Invalid operator!"
        print(f"{num1} {operator} {num2} = {result}")
    
    except ValueError:
        print("Invalid input! Please enter.")

    choice = input("Do you want to perform another calculation? (yes/no): ").lower()
    if choice !="yes":
        print("GoodBye!")
        break