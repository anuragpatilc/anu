# Program to calculate the distance traveled

# Ask the user to enter the speed and time
speed = int(input('Enter the speed: '))
time = int(input('Enter the time:  '))
print('Hour \t\t Distance Traveled')
print('____________________________')

# Add the loop to calculate the Distance for a given time and speed
for x in range(1, time + 1):
    Dist = x * speed
    print(x, '\t\t\t\t', Dist)
