# Ask the user for their financial details
income = float(input("Enter your monthly income: "))
expenses = float(input("Enter your monthly expenses: "))

# Calculate monthly savings
monthly_savings = income - expenses

#projected annual savings
annual_savings = monthly_savings * 12
projected_savings = annual_savings + annual_savings * 0.05  

# Print the results
print(f"Your monthly savings are: {monthly_savings}")
print(f"projected savings after one year, with interest, is: {projected_savings}")
