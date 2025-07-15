theAlphabet = [ "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

inputSentence = input("Enter your message: ")

outputSentence = ""

for char in inputSentence:
    if char.isalpha():
        if char.islower():
            charIndex = theAlphabet.index(char)
            outputSentence += theAlphabet[(charIndex+1) % 26]
        elif char.isupper():
            char = char.lower()
            charIndex = theAlphabet.index(char)
            outputSentence += theAlphabet[(charIndex+1) % 26].upper()
    else:
        outputSentence += char

print(outputSentence)