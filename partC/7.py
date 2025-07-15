phoneNumber = input("Enter your 10 digit phone number in the following format: xxx-xxx-xxxx ")

originalDigits = phoneNumber.replace("-", "")

sum = 0

for digit in originalDigits:
    sum = sum + int(digit)

print("The sum of all digits in your phone number is " + str(sum))