# The program to calculate the entered sec is converted into day-hours-minuets-seconds
# Ask the user to enter the time in seconds
time = int(input('Enter the time in (seconds): '))

if time >= 86400:
    time1 = int(time / 86400)
    print('DAY=', time1)
    a = time1 * 86400
    time2 = time - a
    if time2 >= 3600:
        time3 = int(time2 / 3600)
        b = time3 * 3600
        print('HOURS=', time3)
        time4 = time2 - b
        if time4 >= 60:
            time5 = int(time4 / 60)
            print('MINUTES=', time5)
        else:
            print('SECONDS=', time4)
    else:
        if time2 == 0:
            print('HOURS=', time2)
            print('MINUTES=', time2)
            print('SECONDS=', time2)
        else:
            print('HOURS=', 0)
            print('MINUTES=', 0)
            print('SECONDS=', time2)
elif time >= 3600:
    time6 = int(time / 3600)
    c = time6 * 3600
    print('DAY=', 0)
    print('HOURS=', time6)
    time7 = time - c
    if time7 >= 60:
        time8 = int(time7 / 60)
        print('MINUTES=', time8)
    else:
        if time7 == 0:
            print('MINUTES=', time7)
            print('SECONDS=', time7)
        else:
            print('MINUTES=', 0)
            print('SECONDS=', time7)
else:
    if time >= 60:
        time8 = int(time / 60)
        print('DAYS=', 0)
        print('HOURS=', 0)
        print('MINUTES=', time8)
        print('SECONDS=', 0)
    else:
        print('DAYS=', 0)
        print('HOURS=', 0)
        print('MINUTES=', 0)
        print('SECONDS=', time)







