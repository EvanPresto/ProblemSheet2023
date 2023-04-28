# Author: Evan Preston-Kelly
# Weekly Task 02
# Program prompts the user to enter in two amounds in cents
# The program then adds the two amounts and prints out the total added in euro form 

Amount_One = int(input("Enter amount1 in cent :"))
#sets an int variable to an amount prompted to user called Amount_One
Amount_Two = int(input("Enter amount2 in cent :"))
#sets an int variable to an amount prompted to user called Amount_Two
Total_Amount = (Amount_One + Amount_Two)/100
# Create a variable called Total Amount which is equal to the sum of inputted Amount One + Amount Two . Divides it by 100 to get it in euro form
# 
#  


print("{:.2f}".format(Total_Amount))
# Using f formant with :.2f to show in two decimal form