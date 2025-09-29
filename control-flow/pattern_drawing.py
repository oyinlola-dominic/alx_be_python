def main():
    # Prompt user for the size of the pattern
    try:
        size = int(input("Enter the size of the pattern: "))
        if size <= 0:
            print("Please enter a positive integer.")
            return
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return

    # Initialize row counter for while loop
    row = 0

    while row < size:
        # Print a row of asterisks using a for loop
        for _ in range(size):
            print("*", end="")
        print()  # Move to the next line after each row
        row += 1

if __name__ == "__main__":
    main()

