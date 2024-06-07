def reversed_word(string):
    stack = []
    for char in string:
        stack.append(char)
    
    reversed = ""
    while stack:
        reversed +=  stack.pop() 

    return reversed

print(reversed_word("Raddames"))

# ALTERNATIVE
def word_reversal(string):
    return ''.join(reversed(string))

print(word_reversal("Raddames"))