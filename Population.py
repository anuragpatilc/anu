# Program to calculate the population
s = int(input('Enter the starting number of the organisms: '))
a = int(input('Enter the average daily increase in percentage: '))
n = int(input('Enter the number of days to multiply: '))
per = a / 100
print('Day Approximate \t\t Population')
print('_____________________________________')
print('1', '\t\t\t\t\t\t', s)
for x in range(1, n):
    s = s * 0.3 + s
    print(x + 1, '\t\t\t\t\t\t', s)
