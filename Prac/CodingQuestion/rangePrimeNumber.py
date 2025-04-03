upper = int(input("Enter upper limit : "))
lower = int(input("Enter lower limit : "))

for num in range(lower,upper+1):
    if num>1:
        for i in range(2,num):
            if num % i == 0:
                break
        else:
            print(num)



