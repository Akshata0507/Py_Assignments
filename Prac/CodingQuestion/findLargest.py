num1 = int(input("Enter a Num1 :"))
num2 = int(input("Enter a Num2 :"))
num3 = int(input("Enter a Num3 :"))

if num1 > num2 and num1 > num3:
    print("num 1 is largest number",num1)
elif num2 > num1 and num2 > num3:
    print("num 2 is largest number",num2)
else: 
    print("num 3 is largest number",num2)