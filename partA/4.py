firstWord = input("Enter your first word: ")
secondWord = input("Enter your second word: ")

if firstWord.isupper() and secondWord.isupper():
    print("Opps!")
elif firstWord.isupper() | secondWord.isupper():
    print(firstWord + " " + secondWord)
else:
    print(firstWord + secondWord)