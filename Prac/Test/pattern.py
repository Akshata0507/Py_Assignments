# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15

# 1.intialize variable n=1 to check the current number.
# 2.Loop i from 1 to 5.
# 3.each row, loop i times to print numbers.
# 4.Print numbers on the same line and  to the next line after each line.
# 5.Increment num after print.
# num = 1  


# for i in range(1, 6):
    
#     for j in range(i):
#         print(num, end=" ") 
#         num += 1 
#     print() 


# 3) Write the code to print the following pattern.

# 1

# 1 2

# 1 2 3

# 1 2 3 4

# 1 2 3 4 5

# 1 2 3 4 5 6

# 1 2 3 4 5 6 7

# 1 2 3 4 5 6 7 8

# 1.Loop  1 to 8 .
# 2.In each linw, print numbers  1 to i.
# 3.Move to the next line after print. 

for i in range(1, 9):  
    for j in range(1, i + 1):  
        print(j, end=" ")  
    print()  
