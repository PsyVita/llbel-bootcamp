mostSpentAmount = 0
sum = 0

for dailySpentAmount in range(7):
    dailySpentAmount = int(input("How much did you spend on day " + str(dailySpentAmount+1) + "?"))
    if dailySpentAmount > mostSpentAmount:
        mostSpentAmount = dailySpentAmount
    sum = sum + dailySpentAmount
    
print("The average amount of money used per day is " + str(sum/7) + " baht.")
print("The maximum amount of money used per day is " + str(mostSpentAmount) + " baht.")

