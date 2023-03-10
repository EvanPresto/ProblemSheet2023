def bank():
  Centamount1 = float(input('Enter amount in cents'))
  Centamount2 = float(input('Enter amount in cents'))
  Sum = (Centamount1 + Centamount2)/100
 
  print('The amount is €'"%.2f" % Sum)

bank()