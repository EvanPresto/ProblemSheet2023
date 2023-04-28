#Author: Evan Preston-Kelly
#Program takes an int as an input 
# If the number inputted is even , it divides it by 2, if odd - multiplies it by 3 and adds one
# Program only ends the current value is 1

Number = int(input("Enter number"))
# Prompts user to input a integer and sets it to a variable Number

while Number != 1:
#checking to see if the number is not equal to 1 , if it is not we enter the if statement (control flow)
    if Number % 2 == 0:
        # checking to see if number is even ie no remainder from being divided by 2
        Number = Number / 2
        # reset the number equal to the number divided by 2
        print(int(Number))
        # print the number and as an int to show no decimal places  
    else:
        # if the number fails first if statement ie not even we move to else
        Number = (Number*3) + 1
        # Number is multiplied by 3 and then 1 is added to the number 
        print(int(Number))
        # print the number and as an int to show no decimal places
 