def sumBetween(x,y):
  
    boop = 0
  
    for i in range (x + 1,y):
        boop = boop + i
        print (i)

    return boop

print (sumBetween(5,7))