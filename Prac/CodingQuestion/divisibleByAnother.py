# print("The numbers divible by 13 are:")

# for i in range(1,100):
#     if i % 13 == 0:
#         print(i)




l = [39,68,91,26,89,32]
res = list(filter(lambda x : x % 13 == 0,l))

print(res)