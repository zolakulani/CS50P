# Main function to prompt user and validate plate
def main():
    plate = input("Plate: ")  # Ask user for plate input
    if is_valid(plate):        # Check if plate is valid
        print("Valid")
    else:
        print("Invalid")

# Function to check if a plate is valid according to specific rules
def is_valid(s):
    # Rule 1: Length must be between 2 and 6 characters
    if not (2 <= len(s) <= 6):
        return False
    # Rule 2: The first two characters must be letters
    if not (s[0].isalpha() and s[1].isalpha()):
        return False
    # Rule 3: Plate must contain only letters and numbers
    if not s.isalnum():
        return False
    # Rule 4: Numbers, if present, must be at the end and cannot start with '0'
    number_started = False
    for i in range(len(s)):
        if s[i].isdigit():
            if not number_started:
                number_started = True
                if s[i] == '0':  # First number cannot be '0'
                    return False
            # After numbers start, all following must be digits
        elif number_started:
            return False  # If a letter appears after numbers, invalid
    return True  # All rules passed

main()