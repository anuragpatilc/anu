# This program to calculate the total increase the amount will be calculated by user based

# Constant declaration
total = 0.0

# Enter teh amount u cost per semester
amt = int(input('Enter the amount you cost per semester: '))

# Ask the user to enter number of semester
sem = int(input('Enter the semester: '))

# Ask the user to enter the percentage
per = int(input('Enter the percentage: '))

# calculate the percentage
percentage = per / 100

# Loop to calculate the increment
for x in range(1, sem + 1):
    y = amt * percentage
    total = total + y
    print('semester', x, 'the increased amount is :', total)

print()
t = amt + total
print('The total amount increment in a', sem, 'years is:', t)
