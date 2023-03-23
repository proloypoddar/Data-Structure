# source=[10,20,30,40,50,60]
# k=3
# # temp = []


# # for i in range(0, k):
# #     temp = temp + [source[i]]
# # for i in range(k, len(source)):
# #     source[i-k] = source[i]


# # for i in range(k, len(source)):
# #     source[i] = temp[i-k]
# # print(source)
# for i in range(0,k):
#     val=source[0]
# for j in range(0,len(source)-1):
#     source[j]=source[j+1]
#     source[len(source)-1]=val
# print(source)
##################
def right_shift(a, k):
    n = len(a)
    for i in range(k):
        temp = a[n-1]
        for j in range(n-1, 0, -1):
            a[j] = a[j-1]
        a[0] = temp
    
    return a

a = [1, 2, 3, 4, 5]
k = 2
print(right_shift(a, k))
###################################
def right_shift(a, k):
    n = len(a)
    for i in range(k):
        temp = a[n-1]
        for j in range(n-1, 0, -1):
            a[j] = a[j-1]
        a[0] = temp
    for i in range(k):
        a[i] = 0
    return a

a = [1, 2, 3, 4, 5]
k = 2
print(right_shift(a, k))
