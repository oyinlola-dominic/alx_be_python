def perform_operation(num1, num2, operation):
    """Perform an arithmetic operation based on a word input."""
    operation = operation.lower()
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            raise ValueError("Cannot divide by zero.")
        return num1 / num2
    else:
        raise ValueError("Invalid operation. Use 'add', 'subtract', 'multiply', or 'divide'.")
