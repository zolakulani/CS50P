# Prompt the user to input a text containing emoticons like ":)" or ":("
# and store the result in the variable 'face'
face = input("Please Enter your face: ")

# Replace the text emoticon ":)" with the Unicode smiling emoji "🙂"
face = face.replace(":)", "🙂")

# Replace the text emoticon ":(" with the Unicode frowning emoji "🙁"
face = face.replace(":(", "🙁")

# Print the modified string with emoji replacements
print(face)