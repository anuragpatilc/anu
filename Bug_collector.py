# Program to count the number of bugs collected in a week

# Declaring constant
total = 0.0

# Asking the user number of days u collected the bugs
bug = int(input('How many days in a week u r working as a bug collector: '))

# ERROR correction section
while bug > 7:
    print('ERROR type the correct days')
    bug = int(input('How many days in a week u r working as a bug collector: '))

# the loop of counting the days
for x in range(bug):
    print('Day', x + 1, end=' ')
    col_bugs = int(input('Enter the bugs collected:'))
    total = total + col_bugs

# Printing the total bug collected in a week
print('The total bug collected in a week is:', total)
