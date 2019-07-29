# Program to Diagnostic the wifi rooter
# Variables declaration
a = 'no'
b = 'yes'
print('If the rooter is not working properly do the following steps to solve the problem')
print('Reboot the computer and try to connect.')
c = input('Did that fix the problem?: ')
if c == a:
    print('Reboot the router and try to connect.')
    c = input('Did that fix the problem?: ')
if c == a:
    print('Make sure the cables between the router & modem are plugged in firmly.')
    c = input('Did that fix the problem?: ')
if c == a:
    print('Move the router to a new location and try to connect.')
    c = input('Did that fix the problem?: ')
if c == a:
    print('Get a new router')
if c == b:
    print('congratulation u did it ')


