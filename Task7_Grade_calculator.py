# Program is designed to calculate the grade of the students
# Ask the user to enter the grades
# Enter the first test grade
fir_tst = float(input('Enter the first test grades: '))
# Enter the second test grades
sec_tst = float(input('Enter the second test grades: '))
# Enter the exam grades
exam = float(input('Enter the exam grades: '))
tot_test = fir_tst + sec_tst
tot_grade = tot_test + exam

if fir_tst <= 25:
    if sec_tst <= 25:
        if exam <= 50:
            if exam >= 25:
                if tot_grade >= 50:
                    if tot_grade <= 100:
                        print('Your total grades in the two test is: ', tot_test)
                        print('Your total grades in the exam you enter is: ', exam)
                        print('Your total grates in ths semester: ', tot_grade)
                        if tot_grade >= 80:
                            print('Your grade iS DISTINCTION')
                        else:
                            if tot_grade >= 60:
                                print('Your grade is CREDIT')
                            else:
                                print('Your grade iS PASS ')
                    else:
                        print('ERROR!')
                else:
                    print('Your grade is FAIL bec should take at least 50 grades in final')

            else:
                print('You grade is FAIL bec should take at least 25 grades in exam')
        else:
            print('Invalid exam grade')
    else:
        print('Invalid second test grade')
else:
    print('Invalid first test grade')
