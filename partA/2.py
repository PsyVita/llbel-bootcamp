inputYear = int(input("Enter a year: "))
convertedYear = inputYear - 543

if convertedYear % 400 == 0:
    print(str(inputYear) + " is a leap year.")
elif convertedYear % 100 == 0:
    print(str(inputYear) + " is not a leap year.")
elif convertedYear % 4 == 0:
    print(str(inputYear) + " is a leap year.")
else:
    print(str(inputYear) + " isn't a leap year.")