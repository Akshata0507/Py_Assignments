
# cities=["delhi","Pune","Noida","Mumbai"]
# heros=["aaa","bvf","hudh","dkjh"]
# def print_len(list):
#     print(len(list))

# print_len(cities)
# print_len(heros)

#Q.2    
# heros=["aaa","bvf","hudh","dkjh"]
# # print(heros[0],end=" ")
# # print(heros[1],end=" ")

# def print_list(list):
#     for item in list:
#         print(item,end=" ")
    
# print_list(heros)

#  Q.3
# n = 5
# fact = 1
# for i in range(1, n+1):
#     fact += 1
# print(fact)   

# def cal_fact(n):
#     fact = 1
#     for i in range(1, n+1):
#         fact *= i
#     print(fact)

# cal_fact(5)

#Q.4

def converter(usd_val):
    inr_val = usd_val * 83
    print(usd_val, "USD =",inr_val, "INR")

converter(60)
