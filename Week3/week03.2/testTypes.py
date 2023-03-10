def score(thearray):
    for i in thearray:
     num = thearray[0]
     if num + 2 <= num + i:
         print('Correct')
         
     else:
         print('false')
      
            

score([1,5,6])