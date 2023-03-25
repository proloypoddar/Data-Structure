# # # # # # def factorial(x):
# # # # # #     if x==2:
# # # # # #         return 2
# # # # # #     return x* factorial(x-1)

# # # # # # x=factorial(4)
# # # # # # print(x)
# # # # # ###########################
# # # # # # def fibonacci_numbers(n):
# # # # # #     f = 0
# # # # # #     f2 = 1
# # # # # #     numbers = [f, f2]
# # # # # #     for i in range(n - 2):
# # # # # #         next_fib = f+f2
# # # # # #         numbers+=[next_fib]
# # # # # #         f = f2
# # # # # #         f2 = next_fib
# # # # # #     return numbers
# # # # # # x=fibonacci_numbers(5)
# # # # # # print(x)
# # # # # ############################
# # # # # def fibonacci_number(n):
# # # # #     if n==0 or n==1:
# # # # #         return n
# # # # #     return fibonacci_number(n-1)+fibonacci_number(n-2)
# # # # # x=fibonacci_number(5)
# # # # # print(x)
# # # # # ############################
# # # # # def print_Arr(arr,idx,n):
# # # # #     if idx==n:
# # # # #         return 
# # # # #     print(arr[idx],end='')
# # # # #     print_Arr(arr,idx+1,n)
# # # # # print_Arr([0,4,5,6,7],2,4)
# # # # # #######################$$

# # # # # def base(n,i):
# # # # #     if i==0:
# # # # #         return 1
# # # # #     r=n*base(n,i-1)
# # # # #     return r
# # # # # p=base(3,3)
# # # # # print(p)
# # # # ################################
# # # # # def binary(n):
# # # # #     if n==0:
# # # # #         return ""
# # # # #     return binary(n//2)+str(n%2)
# # # # # x=binary(8)
# # # # # print(x)
# # # # ################## 
# # # # def hocBuilder(height): 
# # # #     if height==0:
# # # #         return 0
# # # #     if height ==1:
# # # #         return 8
# # # #     return 5+hocBuilder(height-1)
# # # # x=hocBuilder(5)
# # # # print(x)
# # # ###############################
# # # def print_one_row(i,end):
# # #     if i==end:
# # #         print(end)
# # #         return
# # #     print(i,end=" ")
# # #     print_one_row(i+1,end)
# # # def print_all_row(end,n):
# # #     if end>n: 
# # #         return
# # #     print_one_row(1,end)
# # #     print_all_row(end+1,n)
# # # print_all_row(1,5)
# # #########################
# # import sys 
# # sys.setrecursionlimit(15000)
# # class FinalQ:
# #     def print(self,array,idx):
# #         if(idx<len(array)):
# #             profit=self.calcProfit(array[idx])
# #             print("Investment",array[idx],"Profit:",profit)
# #             self.print(array,idx+1)
# #     def calcProfit(self,investment):
# #         if investment==25000:
# #             return 0.0
# #         if investment<=100000:
# #             return 4.5 + self.calcProfit(investment-100)
# #         else:
# #             return 8 + self.calcProfit(investment-100)
# # array=[25000,100000,250000,350000] 
# # f = FinalQ() 
# # f.print(array,0)

# ################################################################
# def flattenList(given_list, out_list):
#     if given_list==[]:
#         return []
#     if type (given_list[0])==list:
#         out_list=flattenList(given_list[0],out_list)+flattenList(given_list[1:])
#         return out_list
#     else:
#         out_list=given_list[:1]+flattenList(given_list[1:],out_list)
#         return out_list
# given_list = [1, [2, [3, [4], 5], 6], 7, 8, [9, [[10, 11], 12], 13], 14, [15, [16, [17]]]] 
# output_list = flattenList(given_list, [])
# print(output_list------)
print(4//2)