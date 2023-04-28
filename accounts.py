#Author: Evan Preston-Kelly
#Weekly Task 03
#Prgram takes in a ten digit code 
# Then outputs the account number just showing the last 4 digits and first 6 digits with X 

Account_Number = int(input("Please enter a 10 digit account number"))
Store_Acount_Number = str(Account_Number)
if len(Store_Acount_Number) == 10:
    print("XXXXXXX"+Store_Acount_Number[-4:])
else:
    Account_Number = int(input("Please enter a 10 digit account number"))

