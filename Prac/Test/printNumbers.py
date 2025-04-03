
# 1. Loop  1 to 30.
# 2.condition - if  multiple of 13
# If yes so print "lucky number"
# else number 
# 3.all numbers same line 



for num in range(1, 31):
    
    if num % 13 == 0:
        print("lucky number", end=" ")
    else:
        print(num, end=" ")

