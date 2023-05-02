# Example circular cir_arr
cir_arr = [14, 41, 33, 43, 25, 32, 0, 0]
# n = len(cir_arr)

# # Backward iteration
# counter = n - 1
# for i in range(n):
#     print(cir_arr[counter])
#     counter = (counter - 1) % n

##############################
#Suppose, ‘cir_ar’ has the start position = -3, size = 5 and capacity = 7. Find out the

# def cir_arr(pos,size,cap):
#     last=(pos+size-1)%7
#     print(last)
# cir_arr(-3,5,7)

for i in range(len(cir_arr)-1, 0, -1):
    cir_arr[i] = cir_arr[i-1]
    
cir_arr[0] = 0
print(cir_arr)