# Multiplication table.py

# Ask the user for a number
number = int(input("Enter a number to see its multiplication table: "))

#Use a loop to generate and print the multiplication table
for i in range(1, 11):
    product = number * i
    print(f"{number} x {i} = {product}")
    