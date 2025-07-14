inputYear = input("Enter a year: ")

if int(inputYear) % 4 == 3:
    print(inputYear + " is a leap year.")
else:
    print(inputYear + " isn't a leap year.")