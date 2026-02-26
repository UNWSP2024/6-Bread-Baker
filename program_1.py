# Name: Ariana Fafach
# Date: 2/26/2026
# Title: Program #1: Random Dice



# Program #1: Random Dice
# Write a "randDice" function (with no input) that randomly chooses two numbers between 1 and 6 (inclusive) and then adds them (this is to simulate the rolling of 2 dice).  
# The dice sum will be the output of this function.
import random

def randDice():
    # Write your logic to generate 2 numbers between 1 and 6 here
    number_1 = random.randint(1,6)
    number_2 = random.randint(1,6)

    # Sum 2 numbers
    sum_of_numbers = number_1 + number_2

    # return sum to calling function
    return sum_of_numbers
#########
# Then write a mainline that calls the "randDice" function 100 times in a for loop.  
# The mainline then prints the average of the 100 rolls, rounded to the nearest 0.01.

# Define main function
def main():
    
    # Set total value equal to zero
    total = 0.0

    # For loop runs the randDice function 100 times
    for i in range(100):
       
       # Accumulates the added values of the dice rolls to get the total
       total += randDice()

    # Calculate the average of the 100 rolls
    average = total/100

    # Display the average
    print(f"The average dice roll is: {average:.2f}")

# Call main function
main()