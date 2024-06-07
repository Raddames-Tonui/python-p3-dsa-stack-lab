def evaluate_keystrokes (string):
    stack = []
    for char in string:
        if char  == "<":  # If the character is a backspace
            if len(stack) > 0: # Ensure the stack is not empty before popping
                stack.pop()  # Remove the most recent character from the stack
        else:
            stack.append(char) # Add the current character to the stack
    
    result = ""
    while stack:     # Pop characters from the stack and prepend them to the result string 
        result = stack.pop() + result

    return result

print(evaluate_keystrokes("ac<f<d"))  # Expected output: "ad"


