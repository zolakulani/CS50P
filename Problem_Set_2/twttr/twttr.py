# Prompt the user for input
input = input("Input:")
# Remove any leading/trailing whitespace from the input
input = input.strip()
# Initialize an empty string to store the result
c = ""

# Iterate through each character in the input
for x in input:
    # If the character is a lowercase vowel, skip it
    if (x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u'):
        continue
    # If the character is an uppercase vowel, skip it
    if (x == 'A' or x == 'E' or x == 'I' or x == 'O' or x == 'U'):
        continue
    else:
        # If the character is not a vowel, add it to the result string
        c += ''.join(["", x])
# Print the final result without vowels
print("Output: ", c)