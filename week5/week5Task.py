from datetime import date
today = date.today()
print(today)
days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
dayofweek = today.weekday()
print(dayofweek)
#if dayofweek <= 4:
   # print(weekday)
#else:
    #print('weekend')
#day = input(str("Enter the day"))
#f day in days:
   # print("Its here")
#else:
   # print("No")

def weeks_task():
    today = date.today()
    dayofweek = today.weekday()
    if dayofweek <= 4:
      print('weekday')
    else:
      print('weekend')

print(weeks_task())

