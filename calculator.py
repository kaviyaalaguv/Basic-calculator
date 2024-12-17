def calculator():
    print("Simple Calculator")
    print("Operations: add, sub, multiply, divide")

    # Taking inputs from the user
    operation = input("Enter operation: ").lower()
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Error: Please enter valid numbers.")
        return

    # Perform calculation
    if operation == "add":
        result = num1 + num2
    elif operation == "sub":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            return
        result = num1 / num2
    else:
        print("Error: Unsupported operation.")
        return

    # Display result
    print("Result:", result)

# Run the calculator
calculator()