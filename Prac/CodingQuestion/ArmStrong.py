#addition 

# num = int(input("Enter a Number:"))
# order = len(str(num))

# sum = 0
# temp = num 

# while temp > 0:
#     digit = temp % 10 
#     power = digit ** order
#     sum = sum + power 
#     temp //=10 

# if sum == num:
#     print("It is an armstrong number")
# else :
#     print ("It is not an armstrong number")


#Interval
upper = int(input("Enter upper limit : "))
lower = int(input("Enter lower limit : "))

sum = 0
for num  in range (lower,upper+1):
    order = len(str(num))
    sum = 0
    temp = num 
    while temp > 0:
        digit = temp % 10
        power = digit ** order
        sum = sum  + power
        temp //=10
    if num == sum:
        print(num)
    


