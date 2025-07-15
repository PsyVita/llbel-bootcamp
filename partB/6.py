checkLLBel = False
#checkRocks = False

while True:
    newWord = input("Type in a word: ")
    if newWord == "rocks" and checkLLBel == True:
        #checkRocks = True
        break
    if newWord == "LLBel":
        checkLLBel = True
    else:
        checkLLBel = False

print("Mindset instilled.")