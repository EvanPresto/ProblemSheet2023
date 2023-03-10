import random
The_Num = 11

guess = int(input('Take a guess'))

while guess!=The_Num:
    if guess < The_Num:
     print('Number too low')
     guess = int(input('Take a guess'))
    else:
     print('Number too high')
     guess = int(input('Take a guess'))

print('Correct the number was{}'.format(The_Num))

#use random to get a random number between 1 and 100
