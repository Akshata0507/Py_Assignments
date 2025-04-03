# 1. Write a simple Python program to print an output.
# print ("Hello World")

#2.Write a Python code to check if a number is even or odd
# num = int(input("Enter a number :"))
# if num % 2 == 0:
#     print(f"num is even")
# else:
#     print(f"num is odd")

#3. Write a Python code to concatenate two strings

# str1 = str(input("Enter a String1 :"))
# str2 = str(input("Enter a String2 :"))

# # res = str1+str2 
# res = str1+" "+str2 
# print(res)

#4. Write a Python program to find the maximum of three numbers

# num1 = int(input("Enter a number1 :"))
# num2 = int(input("Enter a number2 :"))

# if (num1 > num2):
#     print(num1)
# else:
#     print(num2)

# num1 = int(input("Enter a number1 :"))
# num2 = int(input("Enter a number2 :"))
# num3 = int(input("Enter a number3 :"))

# print(max(num1,num2,num3))

#5. Write a Python program to count the number of vowels in a string


# inputString = str(input("Enter  a String:"))
# print(sum(1 for char in inputString if char in "aeiouAEIOU"))

#6. Write a Python program to calculate the factorial of a number
# num = int(input("Enter a Number:"))
# fact = 1

# for i in range(1,num+1):
#     fact *= i

# print(fact)
#7.Reverse a string 
# str1  = str(input("Enter a string :"))
# print(str1[::-1])

#8.count a words
# str1  = str(input("Enter a string :"))
# count = 0
# print(len(str1.split()))


#9.whitespace removed
# str1  = str(input("Enter a string :"))
# # count = 0
# str2 = str1.replace(" ","")
# print(len(str2))
# print(str1[4:len(str1)])

#10.7. Write a Python code to convert a string to an integer

# str1 = "Akshata"
# print(int(str1))

#8.Write a Python program to calculate the area of a rectangle
# num1 = int(input("Enter a length:"))
# num2 = int(input("Enter a width:"))

# area = num1*num2
# print(area)

#area of square
# num1 = int(input("Enter a side :"))


# area_square = num1*num1
# print(area_square)

#average
# a = int(input("Enter a"))
# b = int(input("Enter b"))
# c = int(input("Enter c"))

# average = (a+b+c)/2
# print(average)

#9. Write a Python code to merge two dictionaries
# dict1 ={"a":1,"b":2}
# dict2 ={"b":1,"d":2}

# merg={**dict1, **dict2}
# print(merg)

#10. Write a Python program to find common elements in two lists

# list1 =[1,2,3,4,5]
# list2 =[5,2,7,8,2]

# common = list(set(list1) & set(list2))
# print(common)

#11. Write a Python code to remove duplicates from a list
# list1 =[1,2,3,2,5]


# common = list(set(list1))
# print(common)

#12.palindrome 
# str1=str(input("Enter a String"))
# if str1 == str1[::-1]:
#     print("yes its a palindrome")

# else:
#     print("no its not a palindrome")

#longest word 
# str1=str(input("Enter a String"))
# word = str1.split()
# print(len(word))


#17.prime no or not 

num = int(input("Enter a number: "))


if num > 1:
    
    for i in range(2, num):
        if num % i == 0:
            print(f"{num} is not a prime number.")
            break
    else:
        print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")