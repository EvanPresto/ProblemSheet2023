# Author : Evan Preston-Kelly
# Task 06 - function takes in a number and gives the square root of this number


def square_root(number,tolerance = 0.00001):
    x = float(number)
    while True:
        root = 0.5 * (x + number/x)
        if abs(root-x) < tolerance:
            break
        x = root
    return root
            

print(square_root(15))