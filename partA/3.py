university = input("Do you want to go to university?")
input("Which university do you have in mind?")
input("What field of study are you interested in?")

if university.lower() == "yes":
    print("You should apply to LLBel at Chula.")
elif university.lower() == "no":
    print("Too bad!")
else:
    print("Please input a valid response.")