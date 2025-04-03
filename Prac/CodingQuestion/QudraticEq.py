#ax**2 + bx + c = 0 --> Quadratic Equation
  # a,b,c are real number
#a!= 0
import cmath
a = int(input("Enter Number (a!=0):"))
b = int(input("Enter Number:"))
c = int(input("Enter Number:"))

# formula for discriminant 

d = (b**2) -(4*a*c)

root1 = (-b-cmath.sqrt(d))/(2*a)
root2 = (-b+cmath.sqrt(d))/(2*a)

print("the roots are",root1 and root2)