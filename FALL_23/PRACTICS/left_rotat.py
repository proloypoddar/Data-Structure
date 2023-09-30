def left_shift(a):
    temp=a[0] 
    x=1
    while (x<len(a)):
        a[x-1]=a[x]
        x+=1
    a[len(a)-1]=temp
    return a
array=[10,20,30,40,50]
# print(left_shift(array))
time=3
def user(array, time):
    for i in range(0,time):
        left_shift(array)
    return 
user(array,time)
print(array)