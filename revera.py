def reverse():
    x = [1,2,3,4,5]
    y = []
    for i in x[::-1]:
        y.append(i)
    return y

print(reverse())