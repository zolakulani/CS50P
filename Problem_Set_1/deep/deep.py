# Prompt user for the answer and normalize input (lowercase + remove whitespace)
answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").lower().strip()

# Use pattern matching to check against valid answers (modern Python alternative to if/elif)
match(answer):
    case "forty-two" | "forty two" | "42":  # Matches any of these 3 valid forms
        print("Yes")  # Correct answer (from Hitchhiker's Guide to the Galaxy)
    case _:  # Default case (anything else)
        print("No")  # Incorrect answer