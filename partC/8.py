phoneNumber1 = input("Enter your FIRST 10 digit phone number in the following format: xxx-xxx-xxxx ")
phoneNumber2 = input("Enter your SECOND 10 digit phone number in the following format: xxx-xxx-xxxx ")

firstOriginalDigits = phoneNumber1.replace("-", "")
secondOriginalDigits = phoneNumber2.replace("-", "")

firstSum = 0
secondSum = 0

for digit in firstOriginalDigits:
    firstSum += int(digit)
for digit in secondOriginalDigits:
    secondSum += int(digit)

if firstSum == 60:
    firstSum = 0
if secondSum == 60:
    secondSum = 0

if firstSum > secondSum:
    print("The FIRST phone number is more auspicious.")
elif secondSum > firstSum:
    print("The SECOND phone number is more auspicious.")
else:
    print("Both phone numbers are as auspicious as one another.")
