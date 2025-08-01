# Define the main function that handles program execution
def main():
    # Get user input and convert to title case (first letter capitalized) for consistent matching
    item = input("Item: ").title()  # Changed variable name to singular 'item' for clarity

    # Call get_calorie function and print the returned value
    print(get_calorie(item))       # Print the returned value

# Define function to look up calorie information for a given food item
def get_calorie(item):            # Changed parameter name to singular 'item' for consistency
    """
    Returns calorie information for specified fruits using pattern matching.
    Args:
        item (str): The food item to look up
    Returns:
        str: Calorie information or empty string if item not found
    """
    # Use match-case statement (Python 3.10+) to check different fruit cases
    match item:
        case "Apple":  # Case for apples
            return "Calories: 130"

        case "Avocado" | "Cantaloupe": 
            return "Calories: 50"

        case "Sweet Cherries" | "Pear":  # Case for sweet cherries or pears
            return "Calories: 100"

        case "Kiwifruit":  # Case for kiwifruit (note the spelling)
            return "Calories: 90"

        case _:  # Default case - handles any items not listed above
            return ""  # Return empty string for unknown items (per requirements)

# Call main function when script is executed directly
main()