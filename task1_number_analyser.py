# Program to analysis the numerical status
# Take the input from the user
num = float(input('Enter the number to check the status: '))
if num > 0:  # compare with 0
    print('The given number is positive', num)
if num < 0:  # compare with 0
    print('The given number is NEGATIVE', num)
if num == 0:  # compare with 0
    print('The given number is ZERO', num)
num1 = num % 2  # divide with 2 , if it get 0 as output the given number is even or otherwise odd
if num1 == 0:
    print('The given number is EVEN', num)
else:
    print('The given number is ODD', num)

