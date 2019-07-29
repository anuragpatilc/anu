# This program is use to calculate the average rainfall in a given period

# Constant declaration
total = 0.0

# Ask the user to enter the years
year = int(input('Enter the years: '))

# Loop to calculate the rainfall
for x in range(year):
    for y in range(1, 12 + 1):
        print(y, 'st month rain fall in inches: ', end='')
        rain = float(input())
        total = total + rain

# Displaying the results
no_of_months = year * 12
aver = total / no_of_months
print('Number of months is:', no_of_months)
print('Total inches of rainfall is:', total)
print('Average rainfall per month for the entire period is:', format(aver, ',.2f'))
