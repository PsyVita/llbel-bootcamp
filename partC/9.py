thaiInputYear = input("Enter a year: ")

thaiInputYear = thaiInputYear.replace("๐", "0")
thaiInputYear = thaiInputYear.replace("๑", "1")
thaiInputYear = thaiInputYear.replace("๒", "2")
thaiInputYear = thaiInputYear.replace("๓", "3")
thaiInputYear = thaiInputYear.replace("๔", "4")
thaiInputYear = thaiInputYear.replace("๕", "5")
thaiInputYear = thaiInputYear.replace("๖", "6")
thaiInputYear = thaiInputYear.replace("๗", "7")
thaiInputYear = thaiInputYear.replace("๘", "8")
thaiInputYear = thaiInputYear.replace("๙", "9")

convertedYear = int(thaiInputYear) - 543

if convertedYear % 4 == 0:
    print(str(thaiInputYear) + " is a leap year.")
elif convertedYear % 100 == 0 and convertedYear % 400 == 0:
    print(str(thaiInputYear) + " is a leap year.")
else:
    print(str(thaiInputYear) + " isn't a leap year.")


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