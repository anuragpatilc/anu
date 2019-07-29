# This program is used to calculate the factorial of a given number
n = int(input('Enter the number: '))
while n < 0:
    print('The factorial is not is negative number')
    n = int(input('Enter the number: '))
fact = 1
while n > 0:
    fact = fact * n
    n = n - 1
print()
print('Factorial of the number is :', fact)
