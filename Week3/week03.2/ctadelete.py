#Given an array of numbers sorted in increasing order, return true if the array contains 3 adjacent scores that differ from each other by at most 2, such as with {3, 4, 5} , the difference should be the same for both comparisons, so for example 3 is 1 less than 4 and 4 is 1 less than 5
import array

def check_array(the_list):
    for i in the_list:
        first_num = the_list[0]
        dif_next_num = first_num - the_list[1]
        first_num = +i
        print(dif_next_num)


ar_to_check = [1,2,3,4,6]

print(check_array(ar_to_check))