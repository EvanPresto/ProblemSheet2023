List_of_Num = []

Number_Entered = int(input('enter_number (press 0 to quit)'))

while Number_Entered != 0:
    List_of_Num.append(Number_Entered)
    Number_Entered = int(input('enter_number (press 0 to quit)'))


for i in List_of_Num:
    print(i)

sum_of_list = float(sum(List_of_Num) /len(List_of_Num))
print(sum_of_list)