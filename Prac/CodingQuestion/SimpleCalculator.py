num1 = int(input("Enter a num1 : "))
num2 = int(input("Enter a num2 : "))

print("Press 1 for addition \n Press 2 for subtraction \n Press 3 for multiplication \n Press 4 for dividation")

choice = int(input("Enter your choice from 1-4: "))

if choice == 1:
    print("The addition of given two numbers is",num1 + num2)
elif choice == 2:
    print("The subtraction of given two numbers is",num1 - num2)
elif choice == 3:
    print("The multiplication of given two numbers is",num1 * num2)
elif choice == 4:
    print("The dividation of given two numbers is",num1 / num2)
else :
    print("Invalid Input")

