# This program is going to calculate the calories burned in a given time

# Variable declaration
total = 0.0

# Ask the user to enter the minutes worked in the treadmill
work = int(input('Enter the minutes worked in the treadmill: '))

# Error checking loop
while work < 0:
    print('Enter the correct minutes it cont be in negative:', end='')
    work = int(input('Enter the minutes worked in the treadmill: '))

a = work % 5
b = 0
d = 0
if a != 0:
    b = a * 4.2
    work = work - a

# Loop to calculate the calories for every 5 minutes43

for x in range(5, work + 1, 5):
    d = x * 4.2
    print()
    print('calories burned in a', x, 'minutes :', d)

# calculating the total calories burned in the given time
t = b + d
print()
print('The total burned calories in the treadmill is:', t)
