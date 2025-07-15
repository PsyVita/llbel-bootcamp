theAlphabet = [ "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

inputSentence = input("Enter your message: ")
for char in inputSentence:
    if char.isalpha():
        charIndex = char.index
        if char.islower():
            index = list.index(charIndex)
            inputSentence.replace(char, theAlphabet[(index+1) % 26])
        elif char.isupper():
            index = list.index(char)
            inputSentence.replace(char, theAlphabet[(index+1) % 26])