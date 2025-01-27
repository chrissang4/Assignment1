""" Create a program that performs basic arithmetic operations (addition, subtraction, multiplication, and division) on two numbers provided by the user.



 Instructions:



 1. Prompt the user to input two numbers.

 2. Perform the following operations on the two numbers:

    - Addition              - Subtraction

   - Multiplication      - Division

 3. Print the results of each operation with descriptive messages.

 4. Add comments in the code to explain each step."""

#input 1st number(for my case no1 = 4)
no1 = float(input("Enter 1st number: "))

# input 2nd number(for my case no2 = 8)
no2 = float(input("Enter 2nd number: "))

# Addition
addition = no1 + no2

# Subtraction
subtraction = no2 - no1

# Multiplication
multiplication = no1 * no2

# Division
division = no2 / no1

# Printing results in descriptive messages
# Addition results
print(f"The addition results is: {addition}")

# Subtraction results
print(f"The subtraction results is: {subtraction}")

# Multiplication results
print(f"The multiplication results is: {multiplication}")

# Division results
print(f"The Division results is: {division}")