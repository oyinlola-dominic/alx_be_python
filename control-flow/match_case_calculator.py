# Match case Calculator

# Prompt the user for input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operations = input("Enter the operation (+, -, *, /): ")
# perform calculation using the match-case statement
match operations:
    case "+":
        result = num1 + num2
        print(f"The result is {result}")
    case "-":
        result = num1 - num2
        print(f"The result is {result}")
    case "*":
        result = num1 * num2
        print(f"The result is {result}")
    case "/":
        if num2 == 0:
            print("Cannot divide by zero")
        else:
            result = num1 / num2
            print(f"The result is {result}")
    case _:
        print("Invalid operation selected".)
        