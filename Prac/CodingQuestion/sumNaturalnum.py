#positive integers

num = int(input('enter a num :'))
if num < 0:
    print('Please Enter a Natural Number')
else:
    sum = 0
    while num>0:
        sum = sum + num
        num = num -1

    print(sum)

    
