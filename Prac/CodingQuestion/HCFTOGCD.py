def findHCF(x,y):
    if x>y:
        smaller = y
    else:
        smaller = x
    for i in range (1,smaller+1):
        if((x%i == 0) and (y % i == 0)):
            hcf = i
    return hcf

x = int(input('enter a value of x : '))
y = int(input('enter a value of y : '))

print("the given number of hcf is",findHCF(x,y))
