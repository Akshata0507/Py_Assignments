# i=5
# while i >= 1:
#     print(i)
#     i-=1

# print("Loop Ended")

#loops are used to repeat instructions
#while loop 
 
# count = 1
# while count <= 5 :
#     print("Hello")
#     count += 1

# print(count)

#q.1
# i = 1
# while i<=100:
#     print(i)
#     i = i + 1
#q.2
# i = 100
# while i>=1:
#     print(i)
#     i = i - 1

#q.3
 #multiplication table 
# n = int(input("Enter a num:"))
# i = 1
# while i <=10:
#     print(n*i)
#     i +=1 

#q.4
# nums =[1,4,9,16,25,36,49,64,81,100]
# idx = 0
# while idx < len(nums):
#     print(nums[idx])
#     idx +=1

#q.5

nums =(1,4,9,16,25,36,49,64,81,100)
x = 36
i= 0
while i < len(nums):
    if(nums[i] == x):
        print("Found at idx",i)
    else:
        print("Finding...")
    i += 1
