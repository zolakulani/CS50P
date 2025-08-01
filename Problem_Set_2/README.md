# CS50P Problem Set 2

Successfully implemented all problems with particular attention to edge case handling in `plates.py`. Each solution demonstrates robust input validation and string processing.

## Problems Implemented

### 🐫 Camel Case Converter
- Clean string manipulation
- Efficient case detection and conversion
- Handles mixed-case input gracefully

### 🥤 Coke Machine
- Precise currency calculation
- Proper bottle count logic
- Clear user prompts

### � License Plate Validator (`plates.py`)  
**Key Challenge:**  
Implemented Rule 4 (number placement validation) with careful state tracking:
```python
number_started = False
for i in range(len(s)):
    if s[i].isdigit():
        if not number_started:  # First digit check
            number_started = True
            if s[i] == '0':   # Reject leading zero
                return False
        # Subsequent characters must be digits
    elif number_started:       # Letter after digit
        return False
return True