# Get user input and split into three parts: first number, operator, and second number
num1, operator, num2 = input("Expression: ").split()

# Convert input strings to integers for calculation
num1 = int(num1)
num2 = int(num2)

# Perform calculation based on the operator
if operator == '+':
    result = num1 + num2          # Addition
elif operator == '-':
    result = num1 - num2          # Subtraction
elif operator == '*':
    result = num1 * num2          # Multiplication
elif operator == '/':
    if num2 != 0:
        result = num1 / num2      # Division (only if denominator isn't zero)
    else:
        result = "Error: Division by zero"  # Handle division by zero error
else:
    result = "Error: Invalid operator"      # Handle unknown operators

# Print the result with proper formatting
if isinstance(result, str):       # If result is an error message
    print(result)                 # Print the message as-is
else:                            # If result is a number
    print(f"{result:.1f}")        # Print with 1 decimal place (e.g., 2.0)