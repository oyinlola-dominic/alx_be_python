def perform_operation(num1, num2, operation):
    """Perform a basic arithmetic operation on two numbers."""
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 == 0:
            raise ValueError("Cannot divide by zero.")
        return num1 / num2
    else:
        raise ValueError("Invalid operation. Use '+', '-', '*', or '/'.")
