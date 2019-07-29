# Program to calculate the lap times

# Declaring the constants
total = 0.0

# Asking the user to give timing of each loop completes
laps = int(input('Enter the rounds: '))
x = int(input('Enter the time for round 1:'))
a = x
b = x
for i in range(1, laps):
    print('Enter the time for round', i + 1, ':', end='')
    y = int(input())
    total = total + y
    if y >= a:
        a = y
    elif y <= b:
        b = y
c = (total + x) / laps
print('max', a)
print('min', b)
print('average', format(c, ',.2f'))

