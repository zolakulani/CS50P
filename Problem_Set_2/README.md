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

# Twitter Handle Shortener

## Implementation Highlights

- Efficient vowel removal  
- Concise string processing  
- Preserves case formatting  

## Solution Features

### License Plate Validation
- State flag (`number_started`) to track digit sequences  
- Explicit leading zero rejection  
- Early termination for invalid patterns  
- Passes all test cases after iterative refinement  

### Nutrition Facts
- Clean dictionary lookup  
- Simple key validation  
- Clear output formatting  

## Lessons Learned

1. State tracking is crucial for validation rules  
2. Edge cases (like leading zeros) require explicit handling  
3. Iterative testing reveals subtle logic flaws  
4. Python's string methods enable clean solutions  

⏱️ **Total development time**: ~2.5 hours (including 45 minutes debugging plates.py Rule 4)