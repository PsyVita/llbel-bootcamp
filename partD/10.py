inputSentence = input("Enter your message: ")
inputList = inputSentence.split()

for word in inputList:
    i = inputList.index(word)
    if i % 2 == 0:
        inputList[i] = inputList[i].upper()
    if i % 2 == 1:
        inputList[i] = inputList[i].lower()

finalSentence = ' '.join(inputList)
print(finalSentence)