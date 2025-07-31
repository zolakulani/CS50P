def main():
    # Convert dollar string (e.g., "$100") to float and calculate tip based on percentage (e.g., "15%")
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")  # Formats tip to 2 decimal places (e.g., $15.00)


def dollars_to_float(d):
    # Removes '$' from string and converts to float (e.g., "$100" → 100.0)
    d = d.replace("$", "")
    d = float(d)
    return d


def percent_to_float(p):
    # Removes '%' from string, converts to float, and scales to decimal (e.g., "15%" → 0.15)
    p = float(p.replace("%", "")) / 100
    return p


main()  # Runs the program