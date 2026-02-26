# Name: Ariana Fafach
# Date: 2/26/2026
# Title: Program #3: Tax Rate


# Program #3: Tax Rate
# A retail company must file a monthly sales tax report listing the total sales for the month, 
# and the amount of state and county sales tax collected. 
# The state sales tax rate is 5 percent and the county sales tax rate is 2.5 percent.  
# Write a program that asks the user to enter the total sales for the month.  
# From this figure, the application should calculate and display the following:

# The amount of county sales tax.
# The amount of state sales tax.
# The total sales tax (county plus state)
# Use at least one function with input and output in this program


# Get user input for total sales
total_sales = float(input("Enter the total sales for the month:  "))

# Define function
def calculate_tax():

    # Caclulate state tax
    state_tax = total_sales * 0.05
  
    # Calculate county tax
    county_tax = total_sales * 0.025
  
    # Calculate total tax
    total_tax = state_tax + county_tax

    # Display all values
    print(f"The state tax is ${state_tax:,.2f}")
    print(f"The county tax is ${county_tax:,.2f}")
    print(f"The total tax is ${total_tax:,.2f}")
 
 # Call function
calculate_tax()

