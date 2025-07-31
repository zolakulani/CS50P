# Get user greeting, normalize to lowercase and remove whitespace
salute = input("Greeting: ").lower().strip()

# Check greeting type and output appropriate reward
if salute.startswith("hello"):
    print("$0")      # Full greeting gets $0
elif salute.startswith("h"):
    print("$20")     # Just starts with 'h' gets $20
else:
    print("$100")    # All other cases get $100