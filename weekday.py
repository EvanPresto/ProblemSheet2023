# Author : Evan Preston-Kelly
# Task 05 - program outputs whether or not today is a weekday , 
from datetime import datetime
#import datetime module

dt = datetime.now()
# get current date time 

DayEntered = dt.weekday()
# set variable equal to current date time weekday which is an integer 0-6 - Monday - Sunday
print(DayEntered)
if DayEntered <= 4:
    #Check to see if Day entered is less than 4 - 
    print("Weekday")
    # if true prints weekday
else:
    #if not less than 4 it is either 5 or 6 equating to Saturday or Sunday
    print("Weekend")
    # prints Weekend