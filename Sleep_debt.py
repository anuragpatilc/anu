# This program is going to tell exact sleep in a week

keys = 'y'

while keys == 'y':
    # Declaring constants
    total = 0.0
    acc = 56
    for x in range(1, 7 + 1):
        print('How many hours u sleep in', x, 'day in a week:', end='')
        hours = int(input())
        while hours > 24:
            print('you entered the wrong hours')
            print('How many hours u sleep in', x, 'day in a week:', end='')
            hours = int(input())

        total = total + hours

    a = total - acc
    if a > 0:
        print('You sleep more than 8 hours in a week', a, total)
    if a < 0:
        print('you sleep less in this week', a, total)
    if a == 0:
        print('You got correct sleep in this week', a, total)
    keys = input('Do u want another computation: ')
