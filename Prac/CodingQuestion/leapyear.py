#year = 365 days 
#leap year = 366 days ---> once in 4 year

year = int(input("enter a year:"))

if (year % 400 == 0) and (year % 100 == 0):
    print("is a leap year:",year)
elif (year % 4 == 0) and (year % 100 != 0):
    print("is a leap year:",year)
else :
    print("is  not a leap year:",year)