def existo():
    x = [1,2,3,4,5,6]
    num = int(input('Enter number'))
    if num in x:
      return 'True'
    else:
        return 'False'

print(existo())