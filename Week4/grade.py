Grade_Percent = int(input('Enter the percentage'))
if Grade_Percent <= 40:
    print('Fail')
elif Grade_Percent < 50:
    print('Pass')
elif Grade_Percent < 60 :
    print('Merit 2')
elif Grade_Percent < 70 :
    print('Merit 1')
else:
    print('Distinction')